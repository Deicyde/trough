---
declaration: theorem
origin: cited
lean: TauCeti.exists_linearEquiv_comp_fst_eq_comp_snd_comp
statement: formalized
proof: formalized
---

# Schanuel's lemma in automorphism form

If `a : A → E` and `b : B → E` are maps from
projective modules with the same range, then `a ∘ fst` and `b ∘ snd`, as maps `A × B → E`, differ by
an automorphism of `A × B`.

For surjective `a` and `b` this is Schanuel's lemma: the automorphism carries
`ker (a ∘ fst) = ker a × B` onto `ker (b ∘ snd) = A × ker b`.

```lean
TauCeti.exists_linearEquiv_comp_fst_eq_comp_snd_comp.{u_1, u_2, u_3, u_4} {R : Type u_1}
  [Semiring R] {A : Type u_2} {B : Type u_3} {E : Type u_4} [AddCommMonoid E] [_root_.Module R E]
  [AddCommGroup A] [_root_.Module R A] [AddCommGroup B] [_root_.Module R B] [Module.Projective R A]
  [Module.Projective R B] {a : A →ₗ[R] E} {b : B →ₗ[R] E} (h : a.range = b.range) :
  ∃ e, a ∘ₗ LinearMap.fst R A B = b ∘ₗ LinearMap.snd R A B ∘ₗ ↑e
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_linearEquiv_comp_fst_eq_comp_snd_comp`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/Projective/Schanuel.html#TauCeti.exists_linearEquiv_comp_fst_eq_comp_snd_comp).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_linearEquiv_comp_fst_eq_comp_snd_comp`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/Projective/Schanuel.html#TauCeti.exists_linearEquiv_comp_fst_eq_comp_snd_comp)
- [Source of `TauCeti.exists_linearEquiv_comp_fst_eq_comp_snd_comp` in TauCeti/Algebra/Module/Projective/Schanuel.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Module/Projective/Schanuel.lean#L76)
