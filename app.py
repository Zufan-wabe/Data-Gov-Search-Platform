import streamlit as st
import pandas as pd
import requests

# Load the metadata and resources CSV files
metadata_df = pd.read_csv('datasets_metadata1.csv', low_memory=False)
resources_df = pd.read_csv('datasets_resources1.csv', low_memory=False)

# Streamlit app interface
st.title("Dataset Search ")

# Search menu for dataset names or descriptions (using 'notes' as description)
search_term = st.text_input("Search for a dataset by name or keyword")

# Display matching datasets only if a search term is provided
if search_term:
    # Filter datasets based on the search term
    filtered_datasets = metadata_df[
        metadata_df["name"].str.contains(search_term, case=False, na=False) |
        metadata_df["notes"].str.contains(search_term, case=False, na=False)
    ]

    # Display matching datasets
    if not filtered_datasets.empty:
        st.subheader("Matching Datasets")
        # Create a dropdown for users to select a dataset
        dataset_name = st.selectbox(
            "Select a Dataset to Explore",
            filtered_datasets["name"].unique()
        )

        # Get the selected dataset details
        selected_dataset = filtered_datasets[filtered_datasets["name"] == dataset_name].iloc[0]
        st.write(f"### Selected Dataset: {dataset_name}")
        st.write(f"**Description:** {selected_dataset.get('notes', 'No description available')}")

        # Get resources for the selected dataset
        dataset_id = selected_dataset["id"]
        resources = resources_df[resources_df["dataset_id"] == dataset_id]
        if not resources.empty:
            st.write("#### Resources")
            for _, resource in resources.iterrows():
                st.write(f"**Resource Name:** {resource['name']}")
                st.write(f"**Format:** {resource['format']}")
                st.write(f"**Download URL:** {resource['url']}")

                # Option to explore resource
                if st.button(f"Explore {resource['name']}", key=f"{resource['id']}"):
                    resource_url = resource["url"]
                    response = requests.get(resource_url)
                    if response.status_code == 200:
                        try:
                            # Load the data based on format
                            if resource["format"].lower() == "csv":
                                data = pd.read_csv(resource_url)
                            elif resource["format"].lower() == "tsv":
                                data = pd.read_csv(resource_url, delimiter='\t')
                            elif resource["format"].lower() in ["xls", "xlsx"]:
                                data = pd.read_excel(resource_url)
                            else:
                                st.error("Unsupported format for exploration.")
                                continue

                            # Display data exploration results
                            st.write(f"### Exploration of {resource['name']}")
                            st.write("**Top 10 Records:**")
                            st.dataframe(data.head(10))
                            st.write(f"**Number of Records:** {len(data)}")
                            st.write(f"**Number of Columns:** {len(data.columns)}")
                            st.write(f"**Data Types:**")
                            st.write(data.dtypes)
                            st.write("**Basic Statistics:**")
                            st.write(data.describe())
                        except Exception as e:
                            st.error(f"Failed to load the resource data. Error: {e}")
                    else:
                        st.error("Failed to fetch the resource.")
        else:
            st.write("No resources available for this dataset.")
    else:
        st.write("No matching datasets found. Please try a different search term.")
else:
    st.write("Enter a search term above to find datasets.")
