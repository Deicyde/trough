---
declaration: theorem
origin: cited
lean: ContMDiffMap.exists_taylor_coords
statement: formalized
proof: formalized
---

# Taylor's formula in coordinates

A smooth real function on a finite-dimensional space is
its Taylor polynomial of order `n` at `x` plus a combination of the products of `n + 1`
coordinate functions of any finitely-indexed basis, each taken relative to its value at `x`, with
smooth coefficients. When the derivatives of order at most `n` vanish at `x`, this writes the
function as a sum of products of `n + 1` functions vanishing at `x` with smooth functions.

```lean
ContMDiffMap.exists_taylor_coords.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  {ι : Type u_2} [Fintype ι]
  (f : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ ℝ) E ℝ ↑⊤) (x : E)
  (b : Module.Basis ι ℝ E) (n : ℕ) :
  ∃ a,
    ∀ (y : E),
      f y =
        (∑ k ∈ Finset.range (n + 1),
            (↑k.factorial)⁻¹ * (iteratedFDeriv ℝ k (⇑f) x) fun x_1 => y - x) +
          ∑ r, (a r) y * ∏ j, ((b.coord (r j)) y - (b.coord (r j)) x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Taylor's formula to second order](../../../../analysis/part-02/calculus/part-02/taylors-formula-to-second-order.md)

## Lean

Formalized in Tau Ceti as [`ContMDiffMap.exists_taylor_coords`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ContMDiffMap/Hadamard.html#ContMDiffMap.exists_taylor_coords).

## Sources

- [Tau Ceti documentation: `ContMDiffMap.exists_taylor_coords`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ContMDiffMap/Hadamard.html#ContMDiffMap.exists_taylor_coords)
- [Source of `ContMDiffMap.exists_taylor_coords` in TauCeti/Geometry/Manifold/ContMDiffMap/Hadamard.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/ContMDiffMap/Hadamard.lean#L65)
