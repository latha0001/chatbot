from django.shortcuts import render
import requests

def upload_to_aws(request):
    if request.method == 'POST':
        try:
            # Assuming you have the file data in request.FILES['file']
            file_data = request.FILES['file'].read() 

            # Make an HTTP POST request to the Lambda function endpoint
            # Replace with your actual Lambda function ARN
            lambda_arn = 'arn:aws:lambda:your-region:your-account-id:function:your-lambda-function-name' 
            response = requests.post(
                f'https://{lambda_arn}', 
                data=file_data, 
                headers={'Content-Type': 'application/pdf'}  # Adjust content type as needed
            )

            response_data = response.json()
            if response_data['statusCode'] == 200:
                # Handle successful upload (e.g., display a success message)
                return render(request, 'upload_success.html') 
            else:
                # Handle upload errors (e.g., display an error message)
                return render(request, 'upload_error.html', {'error': response_data['body']})

        except Exception as e:
            # Handle general exceptions (e.g., network errors)
            return render(request, 'upload_error.html', {'error': str(e)})

    return render(request, 'upload_form.html')