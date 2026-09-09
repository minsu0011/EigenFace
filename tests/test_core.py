"""Execute original numeric assignments, without GUI or private face images."""
import ast
from pathlib import Path
import numpy as np

def test_original_svd_projection_and_reconstruction():
    tree = ast.parse((Path(__file__).resolve().parents[1] / 'Eigenface_Recognition.py').read_text(encoding='utf-8'))
    names = {'A', 'mean_vector', 'U', 'number', 'topid', 'eigenfaces', 'coefficients', 'reconstructed_images'}
    chosen = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        target = node.targets[0]
        name = target.id if isinstance(target, ast.Name) else target.elts[0].id if isinstance(target, ast.Tuple) else ''
        if name in names:
            chosen.append(node)
    rng = np.random.default_rng(42)
    images = rng.integers(10, 240, (10, 70, 70)).astype(float)
    env = {'np': np, 'image_70701': images}
    # Stop before uint8 display conversion: test original floating-point math.
    chosen = [n for n in chosen if not (isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Attribute) and n.value.func.attr == 'asarray')]
    exec(compile(ast.Module(body=chosen, type_ignores=[]), '<original-numeric-core>', 'exec'), env)
    assert env['eigenfaces'].shape == (10, 4900)
    assert np.allclose(env['reconstructed_images'], images.reshape(10, -1), atol=1e-8)
    assert np.allclose(env['eigenfaces'] @ env['eigenfaces'].T, np.eye(10), atol=1e-8)
