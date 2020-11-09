from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'sostagingstore' # Must be replaced by your <storage_account_name>
    account_key = 'M9F+gOlsYmcIsje5O+J+ajlv0M2KAsua9vm2VAymyl4QlETFdtW2AeYISk1rzQ1110jv0eISIf/lXcj+nJP0tg==>' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'sostagingstore' # Must be replaced by your storage_account_name
    account_key = 'M9F+gOlsYmcIsje5O+J+ajlv0M2KAsua9vm2VAymyl4QlETFdtW2AeYISk1rzQ1110jv0eISIf/lXcj+nJP0tg==>' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None