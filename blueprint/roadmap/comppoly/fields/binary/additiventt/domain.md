---
catalog: module
lean: AdditiveNTT.𝔽q_element_eq_zero_or_eq_one, AdditiveNTT.sDomain, AdditiveNTT.qMap, AdditiveNTT.natDegree_qMap, AdditiveNTT.qMap_ne_zero, AdditiveNTT.degree_qMap, AdditiveNTT.qMap_eval_𝔽q_eq_0, AdditiveNTT.qMap_comp_normalizedW, AdditiveNTT.qMap_is_linear_map, AdditiveNTT.qMap_maps_sDomain, AdditiveNTT.qCompositionChain, AdditiveNTT.qCompositionChain_eq_foldl, AdditiveNTT.normalizedW_eq_qMap_composition, AdditiveNTT.sDomainBasisVectors, AdditiveNTT.sDomainBasisVectors_mem_sDomain, AdditiveNTT.sBasis, AdditiveNTT.sBasis_range_eq, AdditiveNTT.sDomain_eq_image_of_upper_span, AdditiveNTT.sDomain_basis, AdditiveNTT.get_sDomain_basis, AdditiveNTT.get_sDomain_first_basis_eq_1, AdditiveNTT.fintype_sDomain, AdditiveNTT.sDomain_card, AdditiveNTT.splitPointIntoCoeffs, AdditiveNTT.sDomainToFin, AdditiveNTT.finToBinaryCoeffs, AdditiveNTT.finToBinaryCoeffs_sDomainToFin, AdditiveNTT.finToSDomain, AdditiveNTT.sDomainFinEquiv, AdditiveNTT.sDomainFin_bijective
statement: formalized
proof: formalized
---

# Additive NTT Domains

`CompPoly.Fields.Binary.AdditiveNTT.Domain`, in [CompPoly/Fields/Binary/AdditiveNTT/Domain.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean), by Chung Thai Nguyen, Quang Dao.

> Domain-level constructions for the Additive NTT: quotient maps, intermediate
> domains, and the finite-domain bijections used by the algorithm.

`AdditiveNTT.𝔽q_element_eq_zero_or_eq_one` (lemma, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L41))

```lean
lemma 𝔽q_element_eq_zero_or_eq_one : ∀ c : 𝔽q, c = 0 ∨ c = 1
```

`AdditiveNTT.sDomain` (definition, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L58))

```lean
noncomputable def sDomain (i : Fin r) : Subspace 𝔽q L
```

`AdditiveNTT.qMap` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L66))

```lean
noncomputable def qMap (i : Fin r) (h_i_add_1 : i.val + 1 < r) : L[X]
```

`AdditiveNTT.natDegree_qMap` (lemma, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L73))

```lean
lemma natDegree_qMap (i : Fin r) (h_i_add_1 : i.val + 1 < r) :
    (qMap 𝔽q β i h_i_add_1).natDegree = 2
```

`AdditiveNTT.qMap_ne_zero` (lemma, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L100))

```lean
lemma qMap_ne_zero (i : Fin r) (h_i_add_1 : i.val + 1 < r) :
    (qMap 𝔽q β i h_i_add_1) ≠ 0
```

`AdditiveNTT.degree_qMap` (lemma, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L107))

```lean
lemma degree_qMap (i : Fin r) (h_i_add_1 : i.val + 1 < r) :
    (qMap 𝔽q β i h_i_add_1).degree = 2
```

`AdditiveNTT.qMap_eval_𝔽q_eq_0` (theorem, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L114))

```lean
theorem qMap_eval_𝔽q_eq_0 (i : Fin r) (h_i_add_1 : i.val + 1 < r) :
    ∀ c : 𝔽q, (qMap 𝔽q β i h_i_add_1).eval (algebraMap 𝔽q L c) = 0
```

`AdditiveNTT.qMap_comp_normalizedW` (lemma, [line 131](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L131))

```lean
lemma qMap_comp_normalizedW (i : Fin r) (h_i_add_1 : i.val + 1 < r) :
    (qMap 𝔽q β i h_i_add_1).comp (normalizedW 𝔽q β i) =
      normalizedW 𝔽q β ⟨i.val + 1, h_i_add_1⟩
```

`AdditiveNTT.qMap_is_linear_map` (theorem, [line 195](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L195))

```lean
theorem qMap_is_linear_map (i : Fin r) (h_i_add_1 : i.val + 1 < r) :
    IsLinearMap 𝔽q (f := fun inner_p ↦ (qMap 𝔽q β i h_i_add_1).comp inner_p)
```

`AdditiveNTT.qMap_maps_sDomain` (theorem, [line 261](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L261))

```lean
theorem qMap_maps_sDomain (i : Fin r) (h_i_add_1 : i.val + 1 < r) :
    have q_comp_linear_map := qMap_is_linear_map 𝔽q β i h_i_add_1
    have q_eval_linear_map := linear_map_of_comp_to_linear_map_of_eval
      (f := qMap 𝔽q β i h_i_add_1) q_comp_linear_map
    let q_i_map := polyEvalLinearMap (qMap 𝔽q β i h_i_add_1) q_eval_linear_map
    let S_i := sDomain 𝔽q β h_ℓ_add_R_rate i
    let S_i_plus_1 := sDomain 𝔽q β h_ℓ_add_R_rate ⟨i.val + 1, h_i_add_1⟩
    Submodule.map q_i_map S_i = S_i_plus_1
```

`AdditiveNTT.qCompositionChain` (definition, [line 287](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L287))

```lean
noncomputable def qCompositionChain (i : Fin r) : L[X]
```

`AdditiveNTT.qCompositionChain_eq_foldl` (lemma, [line 295](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L295))

```lean
lemma qCompositionChain_eq_foldl (i : Fin r) :
    qCompositionChain 𝔽q β (ℓ := ℓ) (R_rate := R_rate) i =
      Fin.foldl (n := i) (fun acc j =>
        (qMap 𝔽q β ⟨j, by omega⟩ (by change j.val + 1 < r; omega)).comp acc) X
```

`AdditiveNTT.normalizedW_eq_qMap_composition` (lemma, [line 316](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L316))

```lean
lemma normalizedW_eq_qMap_composition (ℓ R_rate : ℕ) (i : Fin r) :
    normalizedW 𝔽q β i = qCompositionChain 𝔽q β (ℓ := ℓ) (R_rate := R_rate) i
```

`AdditiveNTT.sDomainBasisVectors` (definition, [line 335](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L335))

```lean
noncomputable def sDomainBasisVectors (i : Fin r) : Fin (ℓ + R_rate - i) → L
```

`AdditiveNTT.sDomainBasisVectors_mem_sDomain` (lemma, [line 339](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L339))

```lean
lemma sDomainBasisVectors_mem_sDomain (i : Fin r) (k : Fin (ℓ + R_rate - i)) :
    sDomainBasisVectors 𝔽q β h_ℓ_add_R_rate i k
      ∈ sDomain 𝔽q β h_ℓ_add_R_rate i
```

`AdditiveNTT.sBasis` (definition, [line 355](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L355))

```lean
def sBasis (i : Fin r) (h_i : i < ℓ + R_rate) : Fin (ℓ + R_rate - i) → L
```

`AdditiveNTT.sBasis_range_eq` (lemma, [line 359](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L359))

```lean
lemma sBasis_range_eq (i : Fin r) (h_i : i < ℓ + R_rate) :
    β '' Set.Ico i ⟨ℓ + R_rate, h_ℓ_add_R_rate⟩ = Set.range (sBasis β h_ℓ_add_R_rate i h_i)
```

`AdditiveNTT.sDomain_eq_image_of_upper_span` (lemma, [line 398](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L398))

```lean
lemma sDomain_eq_image_of_upper_span (i : Fin r) (h_i : i < ℓ + R_rate) :
    let V_i := Submodule.span 𝔽q (Set.range (sBasis β h_ℓ_add_R_rate i h_i))
    let W_i_map := polyEvalLinearMap (normalizedW 𝔽q β i)
      (normalizedW_is_additive 𝔽q β i)
    sDomain 𝔽q β h_ℓ_add_R_rate i = Submodule.map W_i_map V_i
```

`AdditiveNTT.sDomain_basis` (definition, [line 438](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L438))

```lean
noncomputable def sDomain_basis (i : Fin r) (h_i : i < ℓ + R_rate) :
    Basis (Fin (ℓ + R_rate - i)) 𝔽q (sDomain 𝔽q β h_ℓ_add_R_rate i)
```

`AdditiveNTT.get_sDomain_basis` (lemma, [line 519](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L519))

```lean
lemma get_sDomain_basis (i : Fin r) (h_i : i < ℓ + R_rate) :
    ∀ (k : Fin (ℓ + R_rate - i)),
      (sDomain_basis 𝔽q β h_ℓ_add_R_rate i (by omega)) k =
        eval (β ⟨i + k.val, by omega⟩) (normalizedW 𝔽q β i)
```

`AdditiveNTT.get_sDomain_first_basis_eq_1` (lemma, [line 533](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L533))

```lean
lemma get_sDomain_first_basis_eq_1 (i : Fin r) (h_i : i < ℓ + R_rate) :
    (sDomain_basis 𝔽q β h_ℓ_add_R_rate i (by omega)) ⟨0, by omega⟩ = (1 : L)
```

`AdditiveNTT.fintype_sDomain` (instance, [line 539](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L539))

```lean
noncomputable instance fintype_sDomain (i : Fin r) : Fintype (sDomain 𝔽q β h_ℓ_add_R_rate i)
```

`AdditiveNTT.sDomain_card` (lemma, [line 543](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L543))

```lean
lemma sDomain_card (i : Fin r) (h_i : i < ℓ + R_rate) :
    Fintype.card (sDomain 𝔽q β h_ℓ_add_R_rate i) = (Fintype.card 𝔽q)^(ℓ + R_rate - i)
```

`AdditiveNTT.splitPointIntoCoeffs` (definition, [line 553](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L553))

```lean
def splitPointIntoCoeffs (i : Fin r) (h_i : i < ℓ + R_rate)
    (x : sDomain 𝔽q β h_ℓ_add_R_rate i) : Fin (ℓ + R_rate - i.val) → ℕ
```

`AdditiveNTT.sDomainToFin` (definition, [line 557](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L557))

```lean
noncomputable def sDomainToFin (i : Fin r) (h_i : i < ℓ + R_rate)
    (x : sDomain 𝔽q β h_ℓ_add_R_rate i) : Fin (2^(ℓ + R_rate - i.val))
```

`AdditiveNTT.finToBinaryCoeffs` (definition, [line 565](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L565))

```lean
def finToBinaryCoeffs (i : Fin r) (idx : Fin (2 ^ (ℓ + R_rate - i.val))) :
    Fin (ℓ + R_rate - i.val) → 𝔽q
```

`AdditiveNTT.finToBinaryCoeffs_sDomainToFin` (lemma, [line 570](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L570))

```lean
lemma finToBinaryCoeffs_sDomainToFin (i : Fin r) (h_i : i < ℓ + R_rate)
    (x : sDomain 𝔽q β h_ℓ_add_R_rate i) :
    let pointFinIdx := (sDomainToFin 𝔽q β h_ℓ_add_R_rate i h_i) x
    finToBinaryCoeffs 𝔽q (i := i) (idx := pointFinIdx) = (sDomain_basis 𝔽q β
      h_ℓ_add_R_rate i h_i).repr x
```

`AdditiveNTT.finToSDomain` (definition, [line 596](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L596))

```lean
noncomputable def finToSDomain (i : Fin r) (h_i : i < ℓ + R_rate)
    (idx : Fin (2 ^ (ℓ + R_rate - i.val))) : sDomain 𝔽q β h_ℓ_add_R_rate i
```

`AdditiveNTT.sDomainFinEquiv` (definition, [line 602](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L602))

```lean
noncomputable def sDomainFinEquiv (i : Fin r) (h_i : i < ℓ + R_rate) :
    (sDomain 𝔽q β h_ℓ_add_R_rate i) ≃ Fin (2^(ℓ + R_rate - i.val))
```

`AdditiveNTT.sDomainFin_bijective` (theorem, [line 643](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean#L643))

```lean
theorem sDomainFin_bijective (i : Fin r) (h_i : i < ℓ + R_rate) :
    Function.Bijective (sDomainFinEquiv 𝔽q β h_ℓ_add_R_rate i h_i)
```

## Depends on

- [Frobenius polynomial identities](../../../data/polynomial/frobenius.md)
- [Novel Polynomial Basis](novelpolynomialbasis.md)

## Sources

- [CompPoly/Fields/Binary/AdditiveNTT/Domain.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Domain.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.AdditiveNTT.Domain.json)
