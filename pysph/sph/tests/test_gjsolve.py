from pysph.sph.wc.density_correction import gj_Solve
import numpy as np
import unittest


class TestGjSolve(unittest.TestCase):

    def test_gj_solve(self):
        for _ in xrange(10):
            n = np.random.choice([3, 4])
            mat = 10.0 * (np.random.random_sample((n, n)))
            b = [0.0] * n
            b[0] = 1.0
            result = [0.0] * n
            gj_Solve(np.ravel(mat), b, n, result)
            mat = np.matrix(mat)
            new_b = mat * np.transpose(np.matrix(result))
            new_b = np.ravel(np.array(new_b))
            assert np.allclose(new_b, np.array(b))


if __name__ == '__main__':
    unittest.main()
