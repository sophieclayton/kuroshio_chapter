function plot_tracers_sophie(run_number)

days=1:28;
for day=days
  clf;
  disp(['field= ',num2str(day)])
  st=num2str(run_number - day);
  year=str2num(st(1:4));
  day_of_year=str2num(st(5:end));
  stamp=doy2date(day_of_year+1,year);
  matdate=datestr(stamp,'mmm dd yyyy');
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat',run_number,run_number,day));
  field=[];
œ
  hold on
  imagesc(lon, lat, displacement')
  colormap('copper')
  colorbar()
  axis xy;
 
  hw=5;   % half width of the tracer domain around the site


  % Oct 18
  site_lons=[143.5 143.5 143.5 143.5 143.5 143.5 143.5 143.5];
  site_lats=[36.6102 35.9347 35.8443 35.7645 35.6807 35.5985 35.5208 35.4323];	
  colors={[1,0,0], [0,1,0], [0,0,1], [1,1,1], [1,1,0], [1,0,1], [0,1,1], [0.5,0.5,0.5]};

  % Oct 19
  %site_lons=[144 144 144 144 144 144 144 144];
  %site_lats=[36.0485 36.127 36.2273 36.2977 36.3885 36.471 36.5502 36.6308];
  %colors={[1,0,0], [0,1,0], [0,0,1], [1,1,1], [1,1,0], [1,0,1], [0,1,1], [0.5,0.5,0.5]};

  % Oct 20
  %site_lons=[144.5 144.5 144.5 144.5 144.5 144.5 144.5 144.5];
  %site_lats=[36.5 36.4148 36.3287 36.1602 36.079 35.9967 35.9117 35.831 35.743];
  %colors={[1,0,0], [0,1,0], [0,0,1], [1,1,1], [1,1,0], [1,0,1], [0,1,1], [0.5,0.5,0.5]};
	
  % Oct 21
  %site_lons=[145 145 145 145 145 145 145 145 145.5];
  %site_lats=[35.587 35.6712 35.7537 35.8347 35.916 35.9997 36.0818 36.1672 35.6667];
  %colors={[1,0,0], [0,1,0], [0,0,1], [1,1,1], [1,1,0], [1,0,1], [0,1,1], [0.5,0.5,0.5], [0.3,0.6,0.9]};


  % Oct 22
  %site_lons=[145.5 145.5 145.5 145.5 145.5 145.5 145.5];
  %site_lats=[35.5833 35.5 35.4167 35.4167 35.4167 35.1667 35.1667];
  %colors={[1,0,0], [0,1,0], [0,0,1], [1,1,1], [1,1,0], [1,0,1], [0,1,1]};

  for i=1:size(site_lons,2)
    [lon_index lat_index]=site_indices(lon, lat, site_lons(i), site_lats(i));

    x1=X1(lon_index-hw:lon_index+hw, lat_index-hw:lat_index+hw);
    y1=Y1(lon_index-hw:lon_index+hw, lat_index-hw:lat_index+hw);
    x1=x1(:);
    y1=y1(:);

    plot(x1,y1,'.','Color',cell2mat(colors(i)),'markers',10);
    hold on
    daspect([1,1,1])

    %xlim([min_lon,max_lon])
    %ylim([min_lat,max_lat])

    xlim([137,149])
    ylim([32,40])

    xlabel('Longitude')
    ylabel('Latitude')
    title(matdate)
  end

  drawnow

  %{
  %%%%%%%%%%%%%%  Saving Figures  %%%%%%%%%%%%%%%	
  tracer_path=sprintf('/nobackup1/mdehghani/CS_Trunk/%10.10d/Lagrangian/FTLE/tracer/',run_number);
  if exist(tracer_path)~=7
    mkdir(tracer_path);
  end
  print('-dpng', '-r500', sprintf('%s%10.10d.png',tracer_path,it));
  %}

  hold off
end


end




function [lon_index lat_index]=site_indices(lon, lat, site_lon, site_lat)

  [a lon_index]=min(abs(abs(lon)-site_lon));
  [a lat_index]=min(abs(lat-site_lat));

end
