from gist_search.utils import get_gists


def search_gists(username, description=None, file_name=None):
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return
    gists = get_gists(username)
    if gists is None:
        print('Invalid username {}'.format(username))
        return
    
    results = []
    for gist in gists:
        if description and description.lower() not in gist['description'].lower():
            continue
            
        if file_name:
            found = False
            for f_name in gist['files']:
                found = True
            if not found:
                continue
            
        results.append(gist)
                    
    return results 
        