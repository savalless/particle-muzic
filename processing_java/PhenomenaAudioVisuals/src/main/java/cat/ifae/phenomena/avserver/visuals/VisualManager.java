package cat.ifae.phenomena.avserver.visuals;

import java.util.HashMap;
import java.util.Map;

import cat.ifae.phenomena.avserver.AVServer.PhenoCallback;
import cat.ifae.phenomena.avserver.json.PARAMS;
import cat.ifae.phenomena.avserver.json.PhenomenaCMD;
import cat.ifae.phenomena.viz.particle.MyParticle;
import cat.ifae.phenomena.viz.data.MyParticleData;
import processing.core.PApplet;
import processing.core.PVector;

public class VisualManager implements PhenoCallback {
	private Map<Integer, MyParticle> list = new HashMap<Integer, MyParticle>();
	private PApplet parent;

	public VisualManager(PApplet p) {
		parent = p;
	}

	public void displayParticles() {
		for (MyParticle particle : this.list.values()) {
			particle.display();
		}
	}

	@Override
	public void callback(PhenomenaCMD cmd) {
		switch (cmd.getCMD()) {
		case "ADD":
			MyParticle particle_pic;
			/*ParticlePic partPic = new ParticlePic(parent, cmd.getPARAMS().getId(), cmd.getPARAMS().getMass(),
					cmd.getPARAMS().getDecayTime(), cmd.getPARAMS().getCharge());*/
			PARAMS params = cmd.getPARAMS();
			String message = String.format("Adding particle-pic to list!: ID: %d - Parent: %d type: %s", 
				params.getId(),
				params.getParent(),
				params.getType()
				);
			System.out.println(message);
			String sent[] = {};
			MyParticleData particle_data = new MyParticleData(params.getName(),
														params.getType(),
														params.getComposition(),
														(double) params.getMass(), 
														(double) params.getCharge(),
														(double) params.getDecayTime(),
														sent);
			if (params.getParent() == -1) {
				particle_pic = new MyParticle(this.parent, particle_data);
			}
			else {
				MyParticle parentParticle = list.get(params.getParent());
				PVector location = parentParticle.getLocation();
				particle_pic = new MyParticle(this.parent, location , particle_data);
			}
			this.list.put(cmd.getPARAMS().getId(), particle_pic);
			break;
		case "REMOVE":
			for (int i = 0; i < list.size(); i++) {
				if(list.containsKey(cmd.getPARAMS().getId())) {
					list.remove(cmd.getPARAMS().getId());
					System.out.println("Removing particle-pic from list!");
					break;
				}
			}
			break;
		}
	}
}
