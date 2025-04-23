import argparse


def clone_template(project_name, base):
    print(project_name, base, "uv confirmado para comando")


def main():
    parser = argparse.ArgumentParser(description='Crear nuevo proyecto')
    parser.add_argument('project_name', help='Nombre del nuevo proyecto')
    parser.add_argument('--base', required=True, help='Proyecto base a clonar')

    args = parser.parse_args()

    clone_template(args.project_name, args.base)
