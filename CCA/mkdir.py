def mkdir():
    import os
    from datetime import date
    if not os.path.exists(f'mkdir {date.today()}'):
        try:
            os.system(f'mkdir {date.today()}')
        except PermissionError:
            return print("Permission error occurred.")
    return (print(f'{date.today()} ANALYSIS STARTED'))