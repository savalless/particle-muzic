package cat.ifae.phenomena.viz.particle;


import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.shapes.MyShape;
import cat.ifae.phenomena.viz.shapes.MyWaveRing;
import cat.ifae.phenomena.viz.shapes.MyWaveDisc;
import cat.ifae.phenomena.viz.data.MyParticleData;
import cat.ifae.phenomena.viz.params.MyParams;

import processing.core.PApplet;

import beads.AudioContext;
import processing.core.PVector;

class MyMeson extends MyParticleFamily{

    public MyMeson(PApplet p, PVector location, MyParticleData particleData){
        super(p, location, particleData);

        addMyShapes();
    }

    @Override
    public void addMyShapes(){
        int j = 0;
        for (String q: particleData.getComposition()) {
            myParams = new MyParams(p, particleData,q,j);
            currentCicle = new CurrentCicle(p, myParams.quark.getSpeed());
            shapes.add(new MyWaveRing(p,location, velocity, acceleration,currentCicle,myParams.quark));
        }
        shapes.add(new MyWaveDisc(p,location, velocity, acceleration,myParams.gluon));
    }

    @Override
    public void display(){
        p.text(particleData.getName(), x, y);
        p.blendMode(PApplet.ADD);
        for (MyShape shape: shapes){
            shape.display();
        }
    }

}
