import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;


public class PingPong {

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);

        HttpHandler handler = new PingPongHandler();
        server.createContext("/", handler);

        server.setExecutor(null); // creates a default executor
        server.start();
        System.out.println("Server started on port 8000");
    }

    static class PingPongHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String requestMethod = exchange.getRequestMethod(); // GET, POST, etc.
            String requestURI = exchange.getRequestURI().toString(); // Request URI

            String response;
            if (requestURI.equals("/ping")) {
                response = "{\"response\": \"pong\"}";
            } else if (requestURI.equals("/pings")) {
                response = "{\"response\": \"pongs\"}";
            } else {
                String input = requestURI.substring(1);
                response = "{\"response\": \"pingpongs " + input + "\"}";
            }

            exchange.sendResponseHeaders(200, response.getBytes().length);
            exchange.getResponseHeaders().set("Content-Type", "application/json");
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
}
