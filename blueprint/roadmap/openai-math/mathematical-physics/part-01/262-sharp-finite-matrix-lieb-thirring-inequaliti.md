---
declaration: section
origin: cited
lean: OAI.SharpLiebThirring.sharp_lieb_thirring
statement: formalized
proof: formalized
---

# 262. Sharp finite-matrix Lieb–Thirring inequalities and all equality cases

3 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the sharp one-dimensional Lieb–Thirring inequality for $1/2\lt \gamma\lt 3/2$ and arbitrary finite-matrix potentials *W* ≥ 0 with $\int\mathop{\mathrm{tr}}\nolimits (W^{\gamma+1/2})\lt \infty$: the optimal constant is the scalar one-bound-state value, independent of matrix size. All equality cases are direct sums, in one constant unitary basis, of scalar sech$^{2}$ solitons with independent scales and centers, and zero channels.

## Equality cases in the sharp one-dimensional matrix Lieb–Thirring inequality

We classify all equality cases in the sharp one-dimensional Lieb–Thirring inequality for every finite matrix size and $1/2\lt \gamma\lt 3/2$. For measurable Hermitian positive semidefinite potentials *W* with $\int_\mathbb R\mathop{\mathrm{tr}}\nolimits (W^{\gamma+1/2})\lt \infty$, equality holds precisely for direct sums, in one constant unitary basis, of scalar one-bound-state solitons and zero channels. The nonzero solitons may have independent scales and centers.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/sharp-one-dimensional-lieb-thirring-inequalities-matrix-potentials.pdf).

## Sharp one-dimensional Lieb–Thirring inequalities for matrix potentials

We prove the sharp one-dimensional Lieb–Thirring inequality for every finite matrix size and every exponent $1/2\lt \gamma\lt 3/2$. The optimal constant is the scalar one-bound-state constant, independently of the matrix size. The inequality bounds the full sum of negative eigenvalue moments for every measurable Hermitian positive semidefinite potential *W* satisfying $\int_\mathbb R\mathop{\mathrm{tr}}\nolimits (W^{\gamma+1/2})\lt \infty$. The matrices may have arbitrary rank and need not commute at different points.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/sharp-matrix-lieb-thirring.pdf).

## Sharp one-dimensional Lieb–Thirring constants

We resolve affirmatively the remaining cases of the scalar one-dimensional Lieb–Thirring conjecture: for every $\frac12\lt \gamma\lt \frac32$, the optimal constant is the one-bound-state constant. The estimate holds for every nonnegative potential in $L^{\gamma+1/2}(\mathbb R)$, with all negative eigenvalues included.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result determines the sharp one-dimensional Lieb–Thirring constant for $1/2<\gamma<3/2$. For every nonnegative $W\in L^{\gamma+1/2}(\mathbb R)$, it bounds the full negative-eigenvalue moment of $-d^2/dx^2-W$ by the one-bound-state constant times the potential integral. This constant is optimal and is attained by $(r+1)\mathrm{sech}^2(rx)$, where $r=(\gamma-1/2)^{-1}$. No finite spectral cutoff is imposed.

## Lean: Sharp one-dimensional Lieb–Thirring inequality

```lean
theorem sharp_lieb_thirring : MainClaim
```

Stated in [LiebThirring.lean, line 94](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LiebThirring.lean#L94). Proved in [lean/OAI/Analysis/LiebThirring/Main.lean, line 38](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/LiebThirring/Main.lean#L38). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/262.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/262.md)
