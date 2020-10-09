from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path
from django.shortcuts import render
from django.views.generic import View
from googleapiclient.discovery import build



class HomeView(View):
    def get(self, *args, **kwargs):
        service = build('drive', 'v3')
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))
        service.close()
        context = {}
        return render(self.request, 'home.html', context);


