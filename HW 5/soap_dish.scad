$fn = 150;

module roundedBox(size, radius)
{
	translate([radius, radius, radius]) {
		minkowski()
		{
			cube([size[0]-radius*2, size[1]-radius*2, size[2]-radius*2]);
			sphere(r=radius);
		}
	}
}

difference() {
	difference() {
		difference() {
			roundedBox([100, 70, 60], 15);
			translate([1, 1, 1]) roundedBox([98, 68, 58], 14);
		}
		translate([-30, -30, 30]) cube(size=[300, 300, 300]);
	}
}
