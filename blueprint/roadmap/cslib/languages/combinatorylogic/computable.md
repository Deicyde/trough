---
catalog: module
lean: Cslib.SKI.Computes, Cslib.SKI.Computable, Cslib.SKI.computes_of_total, Cslib.SKI.comp_computes, Cslib.SKI.pair_computes
statement: formalized
proof: formalized
---

# SKI-computable functions

`Cslib.Languages.CombinatoryLogic.Computable`, in [Cslib/Languages/CombinatoryLogic/Computable.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Computable.lean), by Jesse Alama.

> This file defines the notion of SKI-computability for partial functions on natural
> numbers, via Church numerals: a term computes `f : ℕ →. ℕ` if it maps Church numeral
> inputs to Church numeral outputs wherever `f` is defined.
>
> ## Main definitions
>
> - `SKI.Computes`: an SKI term computes a given partial function.
> - `SKI.Computable`: a partial function is SKI-computable if some SKI term computes it.
>
> ## Implementation notes
>
> Unlike `Cslib.URM.Computes`, which is a two-sided equality of `Part` values, this
> predicate is one-sided: it constrains the term's behavior only where the function is
> defined, and says nothing about inputs outside the domain.

`Cslib.SKI.Computes` (definition, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Computable.lean#L42))

> An SKI term `t` computes a partial function `f : ℕ →. ℕ` if,
> for every Church numeral input, `t` applied to the input is a Church numeral
> for the output whenever `f` is defined.

```lean
def Computes (t : SKI) (f : ℕ →. ℕ) : Prop
```

`Cslib.SKI.Computable` (definition, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Computable.lean#L47))

> A partial function `f : ℕ →. ℕ` is SKI-computable if there exists an SKI term that
> computes it.

```lean
def Computable (f : ℕ →. ℕ) : Prop
```

`Cslib.SKI.computes_of_total` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Computable.lean#L52))

> To show that a term computes a total function, it suffices to produce a Church
> numeral for the output on every input.

```lean
theorem computes_of_total {t : SKI} {f : ℕ →. ℕ} (g : ℕ → ℕ)
    (heval : ∀ n, f n = Part.some (g n))
    (hcorrect : ∀ n cn, IsChurch n cn → IsChurch (g n) (t ⬝ cn)) :
    Computes t f
```

`Cslib.SKI.comp_computes` (theorem, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Computable.lean#L60))

> Composition of computable functions is computable.

```lean
theorem comp_computes {f g : ℕ →. ℕ} {tf tg : SKI}
    (hf : Computes tf f) (hg : Computes tg g) :
    Computes (B ⬝ tf ⬝ tg) (f.comp g)
```

`Cslib.SKI.pair_computes` (theorem, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Computable.lean#L69))

> Pairing of computable functions is computable.

```lean
theorem pair_computes {f g : ℕ →. ℕ} {tf tg : SKI}
    (hf : Computes tf f) (hg : Computes tg g) :
    Computes (S ⬝ (B ⬝ NatPair ⬝ tf) ⬝ tg)
      (fun n => Nat.pair <$> f n <*> g n)
```

## Depends on

- [General recursion in the SKI calculus](recursion.md)

## Sources

- [Cslib/Languages/CombinatoryLogic/Computable.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Computable.lean)
