from client import GenerativeImageSpatialUpscaleTilerClient

def main():
    client = GenerativeImageSpatialUpscaleTilerClient()
    res = client.compute_spatial_tiles()
    print('Upscale Spatial Tiler: ' + res['tiler_task_id'] + ' (Factor: ' + str(res['upscale_factor']) + 'x)')
    print('Target: ' + str(res['target_dimensions']['width']) + 'x' + str(res['target_dimensions']['height']) + ' | Tiles: ' + str(res['total_tiles_count']))
    print('Matrix URL: ' + res['tile_layout_matrix_url'])

if __name__ == '__main__':
    main()
