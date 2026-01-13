import os
from azure.storage.blob import BlobServiceClient
import streamlit as st

def upload_to_blob(file, file_name):
    try:
        connection_string = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
        container_name = os.environ.get("BLOB_CONTAINER_NAME")

        if not connection_string or not container_name:
            st.error("Azure Storage connection string or container name not found in environment variables.")
            return None

        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        blob_client.upload_blob(file, overwrite=True)
        return blob_client.url
    except Exception as ex:
        st.error(f"Error uploading to Blob Storage: {ex}")
        return None
