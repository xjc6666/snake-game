from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser

# 定义端口
PORT = 8000

# 创建服务器
Handler = SimpleHTTPRequestHandler
httpd = HTTPServer(("", PORT), Handler)

print(f"服务器启动在端口 {PORT}")
# 自动打开浏览器
webbrowser.open(f'http://localhost:{PORT}')

# 运行服务器
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\n服务器已关闭")
    httpd.server_close() 