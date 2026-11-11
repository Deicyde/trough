---
declaration: theorem
origin: cited
lean: Complex.carlsonRF_duplication
statement: formalized
proof: formalized
---

# Carlson's duplication theorem on the complex slit-plane domain (DLMF 19.26.18)

At most one input may be zero; every transformed node lies strictly in the slit plane.

```lean
Complex.carlsonRF_duplication {x y z : ℂ} (hx : x ∈ Complex.slitPlane ∪ {0})
  (hy : y ∈ Complex.slitPlane ∪ {0}) (hz : z ∈ Complex.slitPlane ∪ {0}) (hxy : x ≠ 0 ∨ y ≠ 0)
  (hxz : x ≠ 0 ∨ z ≠ 0) (hyz : y ≠ 0 ∨ z ≠ 0) :
  x.carlsonRF y z =
    ((x + x.carlsonDuplicationLambda y z) / 4).carlsonRF ((y + x.carlsonDuplicationLambda y z) / 4)
      ((z + x.carlsonDuplicationLambda y z) / 4)
```

## Depends on

- [Carlson's symmetric elliptic integral of the first kind (DLMF 19.16.1)](../../part-01/elliptic-integrals-the-agm-and-jacobi-elliptic-f/carlsons-symmetric-elliptic-integral-of-the-firs.md)

## Proof depends on

- [The duplication theorem for `R_F` (DLMF 19.26.18) at nonnegative real arguments](the-duplication-theorem-for-r-f-dlmf-19-26-18-at.md)
- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`Complex.carlsonRF_duplication`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Carlson/Duplication/Complex.html#Complex.carlsonRF_duplication).

## Sources

- [Tau Ceti documentation: `Complex.carlsonRF_duplication`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Carlson/Duplication/Complex.html#Complex.carlsonRF_duplication)
- [Source of `Complex.carlsonRF_duplication` in TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Carlson/Duplication/Complex.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Carlson/Duplication/Complex.lean#L114)
