from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import socket
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 定义端口
PORT = 8000

def start_server():
    Handler = SimpleHTTPRequestHandler
    
    try:
        httpd = HTTPServer(("", PORT), Handler)
        logger.info(f"服务器启动在端口 {PORT}")
        webbrowser.open(f'http://localhost:{PORT}')
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            logger.info("\n服务器已关闭")
            httpd.server_close()
            
    except socket.error as e:
        logger.error(f"启动服务器失败: 端口 {PORT} 可能已被占用")
        logger.error(f"错误信息: {e}")

if __name__ == "__main__":
    start_server() 