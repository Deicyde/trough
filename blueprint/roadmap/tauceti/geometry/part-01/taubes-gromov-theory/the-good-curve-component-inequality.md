---
declaration: theorem
origin: cited
lean: TauCeti.sum_mul_apply_self_sub_apply_canonical_le
statement: formalized
proof: formalized
---

# The good-curve component inequality

If `e = ∑ m i • C i` is a combination with natural
coefficients of classes which meet pairwise nonnegatively, and `e` is at least `-1` on every
class `C i` of negative square (as for a good class and exceptional spheres), then the virtual
dimensions `d(x) = x · x - κ · x` satisfy `∑ m i d(C i) ≤ d(e)`.

```lean
TauCeti.sum_mul_apply_self_sub_apply_canonical_le.{u_1, u_2} {H : Type u_1} {ι : Type u_2}
  [AddCommGroup H] [Fintype ι] {B : LinearMap.BilinForm ℤ H} {κ e : H} {C : ι → H} {m : ι → ℕ}
  (he : ∑ i, m i • C i = e) (hpos : ∀ {i j : ι}, i ≠ j → 0 ≤ (B (C i)) (C j))
  (hgood : ∀ (i : ι), (B (C i)) (C i) < 0 → -1 ≤ (B e) (C i)) :
  ∑ i, ↑(m i) * ((B (C i)) (C i) - (B κ) (C i)) ≤ (B e) e - (B κ) e
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_mul_apply_self_sub_apply_canonical_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/GoodCycle.html#TauCeti.sum_mul_apply_self_sub_apply_canonical_le).

## Sources

- [Tau Ceti documentation: `TauCeti.sum_mul_apply_self_sub_apply_canonical_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/GoodCycle.html#TauCeti.sum_mul_apply_self_sub_apply_canonical_le)
- [Source of `TauCeti.sum_mul_apply_self_sub_apply_canonical_le` in TauCeti/Geometry/Symplectic/JHolomorphic/GoodCycle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/JHolomorphic/GoodCycle.lean#L141)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TaubesGromov/STATUS.md)
