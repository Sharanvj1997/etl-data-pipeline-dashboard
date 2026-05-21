import pandas as pd

def process_uploaded_file(file_instance):
    file_instance.status = 'PROCESSING'
    file_instance.save()

    try:

        df = pd.read_csv(file_instance.file.path)

        total_rows = len(df)

        success_rows = 0
        failed_rows = 0

        for _, row in df.iterrows():

            email = str(row.get('email', ''))

            if '@' in email and '.com' in email:
                success_rows += 1
            else:
                failed_rows += 1

        file_instance.total_rows = total_rows
        file_instance.success_rows = success_rows
        file_instance.failed_rows = failed_rows
        file_instance.status = 'COMPLETED'

        file_instance.save()

    except Exception:

        file_instance.status = 'FAILED'
        file_instance.save()

