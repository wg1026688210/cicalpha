'''
Created on 2015-11-19

@author: Administrator
'''
from django.shortcuts import render
class LoginMiddleWare:
    def process_request(self,request):
            if not request.user.is_authenticated():
                if request.path !='/dbManager/login1/':
                    
                    return render(request, 'dbManager/login.html')
                else:
                    request.session.set_expiry(10)
                    return None    
            else : 
                request.session.set_expiry(10)
                return None
                
                    
            