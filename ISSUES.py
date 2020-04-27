
https://github.com/machine-learning-apps/ml-template-azure

#CLI commands
{service-principal-name} 
{subscription-id}
{resource-group} 


#goal is to create this
{
  "clientId": "<GUID>",
  "clientSecret": "<GUID>",
  "subscriptionId": "<GUID>",
  "tenantId": "<GUID>",
  (...)
}


az aks list---
      }
    ],
    "name": "Operationalization Subscription",
    "state": "Enabled",
    "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
    "user": {
      "name": "wibuchan@microsoft.com",
      "type": "user"
    }
  }


  {
    "subscription_id": "92c76a2f-0e1c-4216-b65e-abf7a3f34c1e",
    "resource_group": "wibuchan",
    "workspace_name": "wibuchan-workspace"
}



# {
#     "clientId": "your-client-id",
#     "clientSecret": "your-client-secret",
#     "subscriptionId": "your-sub-id",
#     "tenantId": "your-tenant-id",
#     "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
#     "resourceManagerEndpointUrl": "https://management.azure.com",
#     "activeDirectoryGraphResourceId": "https://graph.windows.net",
#     "sqlManagementEndpointUrl": "https://management.core.windows.net:5555",
#     "galleryEndpointUrl": "https://gallery.azure.com/",
#     "managementEndpointUrl": "https://management.core.windows.net"
# }


sp = ServicePrincipalAuthentication(tenant_id="your-tenant-id", # tenantID
                                    service_principal_id="your-client-id", # clientId
                                    service_principal_password="your-client-secret") # clientSecret