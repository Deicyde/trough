---
catalog: module
lean: Cslib.CCS.bisimilarity_par_nil, Cslib.CCS.bisimilarity_par_comm, Cslib.CCS.bisimilarity_nil_par, Cslib.CCS.bisimilarity_par_assoc, Cslib.CCS.bisimilarity_choice_nil, Cslib.CCS.bisimilarity_choice_idem, Cslib.CCS.bisimilarity_choice_comm, Cslib.CCS.bisimilarity_choice_assoc, Cslib.CCS.bisimilarity_congr_pre, Cslib.CCS.bisimilarity_congr_res, Cslib.CCS.bisimilarity_congr_choice, Cslib.CCS.bisimilarity_congr_par, Cslib.CCS.bisimilarity_is_congruence, Cslib.CCS.bisimilarityCongruence
statement: formalized
proof: formalized
---

# Behavioural theory of CCS

`Cslib.Languages.CCS.BehaviouralTheory`, in [Cslib/Languages/CCS/BehaviouralTheory.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean), by Fabrizio Montesi.

> ## Main results
>
> - `CCS.bisimilarityCongruence`: bisimilarity is a congruence in CCS.
>
> Additionally, some standard laws of bisimilarity for CCS, including:
> - `CCS.bisimilarity_par_nil`: P | 𝟎 ~ P.
> - `CCS.bisimilarity_par_comm`: P | Q ~ Q | P
> - `CCS.bisimilarity_choice_comm`: P + Q ~ Q + P

`Cslib.CCS.bisimilarity_par_nil` (theorem, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean#L47))

> P | 𝟎 ~ P

```lean
theorem bisimilarity_par_nil : (par p nil) ~[lts (defs := defs)] p
```

`Cslib.CCS.bisimilarity_par_comm` (theorem, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean#L64))

> P | Q ~ Q | P

```lean
theorem bisimilarity_par_comm : (par p q) ~[lts (defs := defs)] (par q p)
```

`Cslib.CCS.bisimilarity_nil_par` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean#L75))

> 𝟎 | P ~ P

```lean
theorem bisimilarity_nil_par : (par nil p) ~[lts (defs := defs)] p
```

`Cslib.CCS.bisimilarity_par_assoc` (theorem, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean#L86))

> P | (Q | R) ~ (P | Q) | R

```lean
theorem bisimilarity_par_assoc :
    (par p (par q r)) ~[lts (defs := defs)] (par (par p q) r)
```

`Cslib.CCS.bisimilarity_choice_nil` (theorem, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean#L148))

> P + 𝟎 ~ P

```lean
theorem bisimilarity_choice_nil : (choice p nil) ~[lts (defs := defs)] p
```

`Cslib.CCS.bisimilarity_choice_idem` (theorem, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean#L155))

> P + P ~ P

```lean
theorem bisimilarity_choice_idem :
    (choice p p) ~[lts (defs := defs)] p
```

`Cslib.CCS.bisimilarity_choice_comm` (theorem, [line 163](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean#L163))

> P + Q ~ Q + P

```lean
theorem bisimilarity_choice_comm : (choice p q) ~[lts (defs := defs)] (choice q p)
```

`Cslib.CCS.bisimilarity_choice_assoc` (theorem, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean#L170))

> P + (Q + R) ~ (P + Q) + R

```lean
theorem bisimilarity_choice_assoc :
    (choice p (choice q r)) ~[lts (defs := defs)] (choice (choice p q) r)
```

`Cslib.CCS.bisimilarity_congr_pre` (theorem, [line 183](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean#L183))

> P ~ Q → μ.P ~ μ.Q

```lean
theorem bisimilarity_congr_pre :
    (p ~[lts (defs := defs)] q) → (pre μ p) ~[lts (defs := defs)] (pre μ q)
```

`Cslib.CCS.bisimilarity_congr_res` (theorem, [line 202](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean#L202))

> P ~ Q → (ν a) P ~ (ν a) Q

```lean
theorem bisimilarity_congr_res :
    (p ~[lts (defs := defs)] q) → (res a p) ~[lts (defs := defs)] (res a q)
```

`Cslib.CCS.bisimilarity_congr_choice` (theorem, [line 226](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean#L226))

> P ~ Q → P + R ~ Q + R

```lean
theorem bisimilarity_congr_choice :
    (p ~[lts (defs := defs)] q) → (choice p r) ~[lts (defs := defs)] (choice q r)
```

`Cslib.CCS.bisimilarity_congr_par` (theorem, [line 260](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean#L260))

> P ~ Q → P | R ~ Q | R

```lean
theorem bisimilarity_congr_par :
    (p ~[lts (defs := defs)] q) → (par p r) ~[lts (defs := defs)] (par q r)
```

`Cslib.CCS.bisimilarity_is_congruence` (theorem, [line 288](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean#L288))

> Bisimilarity is a congruence in CCS.

```lean
theorem bisimilarity_is_congruence
    (p q : Process Name Constant) (c : Context Name Constant) (h : p ~[lts (defs := defs)] q) :
    (c.fill p) ~[lts (defs := defs)] (c.fill q)
```

`Cslib.CCS.bisimilarityCongruence` (instance, [line 308](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean#L308))

> Bisimilarity is a congruence in CCS.

```lean
instance bisimilarityCongruence : LawfulCongruence (HomBisimilarity (lts (defs := defs)))
```

## Depends on

- [Bisimulation and Bisimilarity](../../foundations/semantics/lts/bisimulation.md)
- [Congruence](../../foundations/syntax/congruence.md)
- [Semantics of CCS](semantics.md)

## Proof depends on

- [Buchi Congruence](../../computability/languages/congruences/buchicongruence.md)

## Sources

- [Cslib/Languages/CCS/BehaviouralTheory.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/BehaviouralTheory.lean)
