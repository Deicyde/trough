---
declaration: theorem
origin: cited
lean: TauCeti.ThricePuncturedSphere.Puncture.plumbingMap_image_union
statement: formalized
proof: formalized
---

# The plumbed four-punctured sphere

For a positive end `q` and a neck length `L > 0`, the
image under the plumbing map of the part `Re z > -L` of the inserted thrice-punctured sphere,
measured in the end coordinate at `∞`, together with the part `Re z < L` of the receiving one,
measured in the end coordinate of `q`, is the four-punctured sphere `ℂ ∖ {0, 1, ψ_{q,L}(1)}`.

```lean
TauCeti.ThricePuncturedSphere.Puncture.plumbingMap_image_union
  {q : TauCeti.ThricePuncturedSphere.Puncture} (hq : q ≠ TauCeti.ThricePuncturedSphere.Puncture.inf)
  {L : ℝ} (hL : 0 < L) :
  q.plumbingMap L ''
        {w | (w ≠ 0 ∧ w ≠ 1) ∧ -L < (TauCeti.ThricePuncturedSphere.Puncture.inf.endCoord w).re} ∪
      {w | (w ≠ 0 ∧ w ≠ 1) ∧ (q.endCoord w).re < L} =
    {w | (w ≠ 0 ∧ w ≠ 1) ∧ w ≠ q.plumbingMap L 1}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ThricePuncturedSphere.Puncture.plumbingMap_image_union`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/ThricePuncturedSphere/Plumbing.html#TauCeti.ThricePuncturedSphere.Puncture.plumbingMap_image_union).

## Sources

- [Tau Ceti documentation: `TauCeti.ThricePuncturedSphere.Puncture.plumbingMap_image_union`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/ThricePuncturedSphere/Plumbing.html#TauCeti.ThricePuncturedSphere.Puncture.plumbingMap_image_union)
- [Source of `TauCeti.ThricePuncturedSphere.Puncture.plumbingMap_image_union` in TauCeti/Analysis/Complex/ThricePuncturedSphere/Plumbing.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/ThricePuncturedSphere/Plumbing.lean#L330)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
