from track_generator import TrackGenerator
from utils import Mode, SimType
from datetime import datetime
import yaml

def make_track_dataset(path_to_config : 'default_config.yaml'):
    '''
    Args:
        path_to_config (str): Path to yaml config file. Use this yaml to change things
        like the number of tracks to generate, track parameters, output options, etc.
    
    Returns:
        None
    '''
    with open(path_to_config, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    
    NUM_TRACKS = config['NUM_TRACKS']
    n_points = config['n_points']
    n_regions = config['n_regions']
    min_bound = config['min_bound']
    max_bound = config['max_bound']
    mode = Mode[config['mode']]
    
    track_width = config['track_width']
    cone_spacing = config['cone_spacing']
    length_start_area = config['length_start_area']
    curvature_threshold = eval(config['curvature_threshold'])
    straight_threshold = eval(config['straight_threshold'])

    plot_track = config['plot_track']
    visualise_voronoi = config['visualise_voronoi']
    create_output_file = config['create_output_file']
    output_folder = config['output_location']
    z_offset = config['z_offset']
    lat_offset = config['lat_offset']
    lon_offset = config['lon_offset']
    sim_type = SimType[config['sim_type']]

    track_gen = TrackGenerator(
                n_points,
                n_regions,
                min_bound,
                max_bound,
                mode,
                plot_track,
                visualise_voronoi,
                create_output_file,
                output_folder,
                track_width,
                cone_spacing,
                length_start_area,
                curvature_threshold,
                straight_threshold,
                z_offset,
                lat_offset,
                lon_offset,
                sim_type
            )
    
    for i in range(NUM_TRACKS):
        out_file_name = f'{i}_{str(sim_type)[str(sim_type).index(".") + 1 : ]}'
        track_gen.create_track(out_file_name)
    
    print(f'Created {NUM_TRACKS} tracks in folder {output_folder}')
    

if __name__ == '__main__':
    make_track_dataset('default_config.yaml')
    print("Done")