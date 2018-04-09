from http.server import HTTPServer ,CGIHTTPRequestHandler,BaseHTTPRequestHandler

class MyHTTPRequestHander(BaseHTTPRequestHandler):

    def do_GET(self):

        #f=open(self.path[1:],'r')
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b'dfdfsdfsdf')
        #f.close()

        
        return b'dfdfdfdfd'


port= 8000
httpd= HTTPServer (( '',port ),MyHTTPRequestHander)
print("starting on port ")
httpd.serve_forever()

# index.html 会默认被调用，没有的话会显示目录下文件
# 不同handler 对 response 的格式要求不一样
