data=readtable("~/Desktop/ground_effect_summary.csv")
hc=data.h_c;
Cl=data.Cl;
figure;
plot(hc,Cl,"o-",'LineWidth',1.5,"MarkerSize",7);
xlabel('Ground clearance, h/c');
ylabel('Lift coefficient, C_L');
grid on;
box on;

exportgraphics(gcf,"~/Desktop/FS_frontwing_project/Cl_vs_hc.png","Resolution", 300);

Cd=data.Cd;
figure;
plot(hc,Cd,"o-",'LineWidth',1.5,"MarkerSize",7);
xlabel('Ground clearance, h/c');
ylabel('Drag coefficient, C_D');
grid on;
box on;

exportgraphics(gcf,"~/Desktop/FS_frontwing_project/Cd_vs_hc.png","Resolution", 300);