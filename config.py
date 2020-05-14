class BaseConfig(object):
    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'MasterUser'

    # Workspace Id for which Embed token needs to be generated
    WORKSPACE_ID = '8394d9ef-8374-4ef9-8fa3-322728221df8'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '773f3a36-7e22-493c-92de-694f8290826f'
    
    # Id of the Azure tenant in which AAD app is hosted
    TENANT_ID = '6b0158e8-72ac-44d5-9602-552a64f04bdc'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '0316ed81-9ca8-494a-92d4-68c84c3873c4'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = ''
    
    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/' + TENANT_ID
    
    # Master user email address. Required only for MasterUser authentication mode
    POWER_BI_USER = 'ds@bcpsoftware.com'
    
    # Master user email password. Required only for MasterUser authentication mode
    POWER_BI_PASS = 'BlackieK5!'