---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.UpperBoundSimplicialSpheresWanted.Combinatorics.UpperBoundSimplicialSpheresProblem.E, MathlibExt.Combinatorics.UpperBoundSimplicialSpheresWanted.Combinatorics.UpperBoundSimplicialSpheresProblem.cyclicH, MathlibExt.Combinatorics.UpperBoundSimplicialSpheresWanted.Combinatorics.UpperBoundSimplicialSpheresProblem.cyclicPolytopeFaceCount, MathlibExt.Combinatorics.UpperBoundSimplicialSpheresWanted.Combinatorics.UpperBoundSimplicialSpheresProblem.upper_bound_theorem_simplicial_spheres
statement: formalized
---

# Upper bound theorem for simplicial spheres

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/upper-bound-theorem-for-simplicial-spheres/index.html).

## Euclidean space $\mathbb{R}^d$

For a natural number $d$, the real Euclidean space
$\mathbb{R}^d$ of dimension $d$ with its standard inner product; it is the ambient space of a
$(d-1)$-dimensional sphere.

Formalized by `MathlibExt.Combinatorics.UpperBoundSimplicialSpheresWanted.Combinatorics.UpperBoundSimplicialSpheresProblem.E`, an abbreviation declared in [WantedExt/Combinatorics/UpperBoundSimplicialSpheresWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/UpperBoundSimplicialSpheresWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/upper-bound-theorem-for-simplicial-spheres/index.html#e).

## h-vector of the cyclic polytope

For natural numbers $n$, $d$ and $j$, let
$m = \min(j, d - j)$; the value is $\binom{n - d - 1 + m}{m}$, where subtraction is truncated
at $0$. For $n \ge d + 1$ and $j \le d$ this is the entry $h_j$ of the h-vector of the cyclic
polytope $C(n, d)$, namely $h_j = \binom{n-d-1+j}{j}$ for $j \le d/2$ and $h_j = h_{d-j}$
otherwise. For $j > d$ the value is $1$.

Formalized by `MathlibExt.Combinatorics.UpperBoundSimplicialSpheresWanted.Combinatorics.UpperBoundSimplicialSpheresProblem.cyclicH`, a definition declared in [WantedExt/Combinatorics/UpperBoundSimplicialSpheresWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/UpperBoundSimplicialSpheresWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/upper-bound-theorem-for-simplicial-spheres/index.html#cyclic-h).

## Face numbers of the cyclic polytope

For natural numbers $n$, $d$ and $k$, the value is

$$
\sum_{j=0}^{k+1} \binom{d-j}{k+1-j} \binom{n-d-1+m_j}{m_j}, \qquad m_j = \min(j, d-j),
$$

where subtraction is truncated at $0$. The second binomial coefficient is the cyclic polytope
h-vector entry $h_j$, so for $k < d$ and $n \ge d + 1$ this sum is the inverse h-to-f transform
of the h-vector of the cyclic polytope $C(n, d)$, that is, the number of $k$-dimensional faces
of $C(n, d)$.

Formalized by `MathlibExt.Combinatorics.UpperBoundSimplicialSpheresWanted.Combinatorics.UpperBoundSimplicialSpheresProblem.cyclicPolytopeFaceCount`, a definition declared in [WantedExt/Combinatorics/UpperBoundSimplicialSpheresWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/UpperBoundSimplicialSpheresWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/upper-bound-theorem-for-simplicial-spheres/index.html#cyclic-polytope-face-count).

## Upper bound theorem for simplicial spheres

Let $d$, $n$ and $k$ be natural numbers
with $k < d$, and let $X$ be a finite simplicial $(d-1)$-sphere, that is, a finite geometric
simplicial complex in $\mathbb{R}^d$ whose underlying space is homeomorphic to the unit sphere
of $\mathbb{R}^d$. If $X$ has $n$ vertices, then the number of $k$-dimensional faces of $X$
(faces with $k + 1$ vertices) is at most

$$
\sum_{j=0}^{k+1} \binom{d-j}{k+1-j} \binom{n-d-1+m_j}{m_j}, \qquad m_j = \min(j, d-j),
$$

with subtraction truncated at $0$; for $n \ge d + 1$ this is the number of $k$-dimensional
faces of the cyclic polytope $C(n, d)$.

## Sources

- R.P. Stanley, 'The upper bound conjecture and Cohen–Macaulay rings', Studies in Appl. Math. 54 (1975) 135–142. Conjecture: T.S. Motzkin (1957); polytope case: P. McMullen, 'The maximum numbers of faces of a convex polytope', Mathematika 17 (1970) 179–184. §142 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `upper_bound_simplicial_spheres` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.UpperBoundSimplicialSpheresWanted.Combinatorics.UpperBoundSimplicialSpheresProblem.upper_bound_theorem_simplicial_spheres` is written with `theorem_wanted` in [WantedExt/Combinatorics/UpperBoundSimplicialSpheresWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/UpperBoundSimplicialSpheresWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/upper-bound-theorem-for-simplicial-spheres/index.html#upper-bound-theorem-simplicial-spheres).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Upper bound theorem for simplicial spheres](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/upper-bound-theorem-for-simplicial-spheres/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/polytopes-simplicial-complexes/upper-bound-theorem-for-simplicial-spheres)
