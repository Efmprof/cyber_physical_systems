$fn = 100;
echo(version=version());

// size is a vector [w, h, d]
module roundedBox(size, radius)
{
	translate([radius, radius, radius]) {
		minkowski()
		{
			cube(size);
			sphere(r=radius);
		}
	}
	
}
difference() {
	difference() {
		difference() {
			roundedBox([100,70,60], 15);
			translate([2, 2, 2]) roundedBox([98,68,28], 14);
		}
		translate([0, 0, 30]) cube(size=[300, 300, 300]);
	}
	
    

}
