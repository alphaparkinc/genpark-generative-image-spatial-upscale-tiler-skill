class GenerativeImageSpatialUpscaleTilerClient:
    def compute_spatial_tiles(self, input_width=1024, input_height=1024, upscale_factor=4, tile_dimension=1024, overlap_pixels=128):
        target_width = input_width * upscale_factor
        target_height = input_height * upscale_factor
        return {
            'tiler_task_id': 'ups_tile_7719',
            'input_dimensions': {'width': input_width, 'height': input_height},
            'target_dimensions': {'width': target_width, 'height': target_height},
            'upscale_factor': upscale_factor,
            'total_tiles_count': 25,
            'overlap_pixels': overlap_pixels,
            'feather_blending_gradient': 'COSINE_ALPHA_RAMP',
            'seam_artifact_mitigation': True,
            'tile_layout_matrix_url': 'https://media.canvas.genpark.ai/tiles/ups_tile_7719.json'
        }
