---
declaration: theorem
origin: cited
lean: TauCeti.iwasawaHomeomorph_symm_toGL
statement: formalized
proof: formalized
---

# The Iwasawa decomposition of `GL n ℝ` restricts to `SL n ℝ`

the factors in `GL n ℝ` of a
matrix of determinant one are the images under `toGL` of its factors in `SL n ℝ`.

```lean
TauCeti.iwasawaHomeomorph_symm_toGL {n : ℕ} (g : Matrix.SpecialLinearGroup (Fin n) ℝ) :
  (TauCeti.iwasawaHomeomorph ℝ n).symm (Matrix.SpecialLinearGroup.toGL g) =
    (⟨Matrix.SpecialLinearGroup.toGL ↑((TauCeti.iwasawaSLHomeomorph n).symm g).1, ⋯⟩,
      ⟨Matrix.SpecialLinearGroup.toGL ↑((TauCeti.iwasawaSLHomeomorph n).symm g).2.1, ⋯⟩,
      ⟨Matrix.SpecialLinearGroup.toGL ↑((TauCeti.iwasawaSLHomeomorph n).symm g).2.2, ⋯⟩)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.iwasawaHomeomorph_symm_toGL`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/SpecialLinearGroup/Iwasawa.html#TauCeti.iwasawaHomeomorph_symm_toGL).

## Sources

- [Tau Ceti documentation: `TauCeti.iwasawaHomeomorph_symm_toGL`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/SpecialLinearGroup/Iwasawa.html#TauCeti.iwasawaHomeomorph_symm_toGL)
- [Source of `TauCeti.iwasawaHomeomorph_symm_toGL` in TauCeti/LinearAlgebra/Matrix/SpecialLinearGroup/Iwasawa.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/SpecialLinearGroup/Iwasawa.lean#L197)
