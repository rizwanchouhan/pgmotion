from hmr4d.configs import parse_args_to_cfg, register_store_pgmotion
from hmr4d.utils.vis.rich_logger import print_cfg

if __name__ == "__main__":
    register_store_pgmotion()
    cfg = parse_args_to_cfg()
    print_cfg(cfg, use_rich=True)
