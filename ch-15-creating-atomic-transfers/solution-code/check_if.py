def is_account_opted_in(account_assets, provided_asset_id):
    for asset_info in account_assets:
        current_asset_id = asset_info["asset-id"]

        if(current_asset_id == provided_asset_id):
            print("The account is already opted-in")
            opted_in = True
            return opted_in

    print("The account is not opted-in")
    print("Opting account in now")
    opted_in = False
    return opted_in