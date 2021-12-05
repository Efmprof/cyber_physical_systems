cs = 10; // TRY TO CHANGE ME!!!
xoffset = cs*4;

module triangle() {
    translate([cs, 0, 0])     cube(cs);
    translate([cs, cs, 0])     cube(cs);
    cube(cs);
}

triangle();

translate([xoffset, 0, 0]) {
    triangle();
    translate([cs, cs, cs])     cube(cs);
}

translate([xoffset*2, 0, 0]) {
    rotate([0, 0, -90]) translate([-cs*2, 0, 0]) triangle();
    translate([0, cs, cs])     cube(cs);
}

translate([xoffset*3, 0, 0]) {
    triangle();
    translate([cs, 0, cs])     cube(cs);
}

translate([xoffset*4, 0, 0]) {
    triangle();
    translate([cs*2, 0, 0])     cube(cs);
}

translate([xoffset*5, 0, 0]) {
    rotate([0, 0, -90]) translate([-cs*2, cs, 0]) triangle();
    translate([0, cs, 0])     cube(cs);
}

translate([xoffset*6, 0, 0]) {
    rotate([0, 0, -90]) translate([-cs*2, 0, 0]) triangle();
    translate([0, cs*2, 0])     cube(cs);
}


