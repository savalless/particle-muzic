package cat.ifae.phenomena.avserver.AVServer;

import processing.core.PApplet;
import processing.net.*;

public class AVServer extends PApplet {
	int port = 1234;
	Server server;
	JsonHandler handleJson;
	ListManager manageList;

	public static void main(String[] args) {
		PApplet.main("cat.ifae.phenomena.avserver.AVServer.AVServer");
	}

	public void settings() {
		size(1920, 1200, P3D);
		//fullScreen(P3D);
	}

	public void setup() {
		frameRate(24);
		smooth();
		// colorMode(HSB, 360, 100, 100);
		server = new Server(this, port);
		handleJson = new JsonHandler();
		manageList = new ListManager(this);
	}

	public void draw() {
		background(0);
		Client thisClient = server.available();
		if (thisClient != null) {
			try {
				String receivedString = thisClient.readString();
				manageList.updateList(handleJson.parse(receivedString));
			} catch (Exception ex) {
				System.out.println("Failed loading particle!");
				ex.printStackTrace();
			}
		}
		manageList.visualize();
	}

	public void keyPressed() {
		/*
		 * if (key == 'l') { println(manageList.getList()); }
		 */
	}
}
