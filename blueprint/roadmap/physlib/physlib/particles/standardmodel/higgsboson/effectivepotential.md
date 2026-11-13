---
declaration: module
origin: cited
lean: StandardModel.HiggsField.EffectivePotential, StandardModel.HiggsField.EffectivePotential.IsInvariant, StandardModel.HiggsField.EffectivePotential.IsInvariant.eq_on_orbits, StandardModel.HiggsField.EffectivePotential.IsInvariant.eq_of_norm_eq, StandardModel.HiggsField.EffectivePotential.IsInvariant.factors_through_norm, StandardModel.HiggsField.EffectivePotential.HasMaxMassDimLE, StandardModel.HiggsField.EffectivePotential.polynomial, StandardModel.HiggsField.EffectivePotential.polynomial_totalDegree
statement: formalized
proof: formalized
---

# The effective potential of the Higgs field

The module `Physlib.Particles.StandardModel.HiggsBoson.EffectivePotential`, [Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean): 20 declarations, 8 with a docstring.

> We define a general effective potential for the Higgs field.
> For this we define two properties of the potential: invariance under the gauge group, and a
> maximum mass dimension.
>
> Given these, we prove that the potential can be expressed as a polynomial in the norm of the
> Higgs field.

**`StandardModel.HiggsField.EffectivePotential`**, an abbrev, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L34).

> A general potential of the Higgs field.

```lean
abbrev EffectivePotential : Type
```

## A. The invariance of the general potential under the gauge group

**`StandardModel.HiggsField.EffectivePotential.IsInvariant`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L46).

> The proposition that the general potential is invariant under
> the global action of the gauge group.

```lean
def IsInvariant (V : EffectivePotential) : Prop
```

**`StandardModel.HiggsField.EffectivePotential.IsInvariant.eq_on_orbits`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L52).

> An invariant potential is equal on gauge orbits.

```lean
lemma eq_on_orbits {φ1 φ2 : HiggsVec} {V : EffectivePotential} (h : IsInvariant V)
    (hφ : ∃ g : GaugeGroupI, HiggsVec.repGaugeGroupI g φ2 = φ1) :
    V φ1 = V φ2
```

**`StandardModel.HiggsField.EffectivePotential.IsInvariant.eq_of_norm_eq`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L59).

> An invariant potential is equal on Higgs vectors with identical norms.

```lean
lemma eq_of_norm_eq {φ1 φ2 : HiggsVec} {V : EffectivePotential} (h : IsInvariant V)
    (hφ : ‖φ1‖ = ‖φ2‖) :
    V φ1 = V φ2
```

**`StandardModel.HiggsField.EffectivePotential.IsInvariant.factors_through_norm`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L63).

```lean
lemma factors_through_norm {V : EffectivePotential} (h : IsInvariant V) :
    ∃ (f : ℝ → ℝ), V = f ∘ norm
```

## B. Maximum mass dimension

**`StandardModel.HiggsField.EffectivePotential.HasMaxMassDimLE`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L81).

> The proposition that the potential `V` has a maximum mass dimension
> less then or equal to `n` - also implying it is a polynomial.

```lean
def HasMaxMassDimLE (V : EffectivePotential) (n : ℕ) : Prop
```

**`StandardModel.HiggsField.EffectivePotential.polynomial`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L87).

> The polynomial associated to a potential `V` with a maximum mass dimension
> less than or equal to `n`.

```lean
def polynomial (V : EffectivePotential) {n : ℕ} (h : HasMaxMassDimLE V n) :
    MvPolynomial (Fin 4) ℝ
```

**`StandardModel.HiggsField.EffectivePotential.polynomial_totalDegree`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L90).

```lean
lemma polynomial_totalDegree {V : EffectivePotential} {n : ℕ} (h : HasMaxMassDimLE V n) :
    (polynomial V h).totalDegree ≤ n
```

**`StandardModel.HiggsField.EffectivePotential.apply_eq_polynomial`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L93).

```lean
lemma apply_eq_polynomial {V : EffectivePotential} {n : ℕ} (h : HasMaxMassDimLE V n)
    (φ : HiggsVec) : V φ = (polynomial V h).eval φ.toRealScalars
```

## C. Terms of a given mass dimension

**`StandardModel.HiggsField.EffectivePotential.termOfMassDim`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L103).

> The part of a potential at a given mass-dimension.

```lean
def termOfMassDim (V : EffectivePotential) {n : ℕ} (h : HasMaxMassDimLE V n) (m : ℕ) :
    HiggsVec → ℝ
```

**`StandardModel.HiggsField.EffectivePotential.termOfMassDim_eq_zero_of_max_lt`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L106).

```lean
lemma termOfMassDim_eq_zero_of_max_lt {V : EffectivePotential} {n : ℕ} (h : HasMaxMassDimLE V n)
    {m : ℕ} (hm : n < m) (φ : HiggsVec) :
    termOfMassDim V h m φ = 0
```

**`StandardModel.HiggsField.EffectivePotential.termOfMassDim_homogeneity`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L113).

```lean
lemma termOfMassDim_homogeneity {V : EffectivePotential} {n : ℕ} (h : HasMaxMassDimLE V n) (m : ℕ)
    (φ : HiggsVec) (t : ℝ) : termOfMassDim V h m (t • φ) = t ^ m * termOfMassDim V h m φ
```

**`StandardModel.HiggsField.EffectivePotential.apply_eq_sum_termOfMassDim`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L126).

```lean
lemma apply_eq_sum_termOfMassDim {V : EffectivePotential} {n : ℕ} (h : HasMaxMassDimLE V n)
    (φ : HiggsVec) :
    V φ = ∑ m ∈ Finset.range (n + 1), termOfMassDim V h m φ
```

**`StandardModel.HiggsField.EffectivePotential.apply_smul_eq_sum_termOfMassDim`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L139).

```lean
lemma apply_smul_eq_sum_termOfMassDim {V : EffectivePotential} {n : ℕ} (h : HasMaxMassDimLE V n)
    (φ : HiggsVec) (t : ℝ) :
    V (t • φ) = ∑ m ∈ Finset.range (n + 1), t ^ m * termOfMassDim V h m φ
```

**`StandardModel.HiggsField.EffectivePotential.termOfMassDim_isInvariant`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L145).

```lean
lemma termOfMassDim_isInvariant {V : EffectivePotential} {n : ℕ} (h : HasMaxMassDimLE V n)
    (m : ℕ) (hV : IsInvariant V) : IsInvariant (termOfMassDim V h m)
```

**`StandardModel.HiggsField.EffectivePotential.termOfMassDim_eq_mul_norm`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L172).

```lean
lemma termOfMassDim_eq_mul_norm {V : EffectivePotential} {n : ℕ}
    (h : HasMaxMassDimLE V n) (m : ℕ) (hV : IsInvariant V) (φ : HiggsVec) :
    ∃ c, termOfMassDim V h m φ = c * ‖φ‖ ^ m
```

**`StandardModel.HiggsField.EffectivePotential.termOfMassDim_zero_of_odd`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L180).

```lean
lemma termOfMassDim_zero_of_odd {V : EffectivePotential} {n : ℕ} (h : HasMaxMassDimLE V n) (m : ℕ)
    (hV : IsInvariant V) (φ : HiggsVec) (hodd : Odd m)  :
    termOfMassDim V h m φ = 0
```

## D. Potential in terms of the norm of the Higgs field

**`StandardModel.HiggsField.EffectivePotential.apply_eq_sum_even_termOfMassDim`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L194).

```lean
lemma apply_eq_sum_even_termOfMassDim {V : EffectivePotential} {n : ℕ} (h : HasMaxMassDimLE V n)
    (hV : IsInvariant V) (φ : HiggsVec) :
    V φ = ∑ m ∈ Finset.range (n / 2 + 1), termOfMassDim V h (2 * m) φ
```

**`StandardModel.HiggsField.EffectivePotential.apply_eq_sum_even_termOfMassDim_fin`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L216).

```lean
lemma apply_eq_sum_even_termOfMassDim_fin {V : EffectivePotential} {n : ℕ} (h : HasMaxMassDimLE V n)
    (hV : IsInvariant V) (φ : HiggsVec) :
    V φ = ∑ m : Fin (n/2 + 1), termOfMassDim V h (2 * m) φ
```

**`StandardModel.HiggsField.EffectivePotential.apply_eq_sum_norm_pow`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean#L222).

> The potential is equal to the sum of norms to even powers.

```lean
lemma apply_eq_sum_norm_pow {V : EffectivePotential} {n : ℕ} (h : HasMaxMassDimLE V n)
    (hV : IsInvariant V) (φ : HiggsVec) :
    ∃ c : Fin (n/2 + 1) → ℝ, V φ = ∑ m, c m • ‖φ‖ ^ (2 * m.1)
```

## Depends on

- [The Higgs field](basic.md)

## Sources

- [Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/EffectivePotential.lean)
