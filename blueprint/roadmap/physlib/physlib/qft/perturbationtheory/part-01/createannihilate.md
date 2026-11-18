---
declaration: module
origin: cited
lean: CreateAnnihilate, CreateAnnihilate.eq_create_or_annihilate, CreateAnnihilate.normalOrder, CreateAnnihilate.not_normalOrder_annihilate_iff_false, CreateAnnihilate.sum_eq, CreateAnnihilate.CreateAnnihilate_card_eq_two
statement: formalized
proof: formalized
---

# Creation and annihilation parts of fields

The module `Physlib.QFT.PerturbationTheory.CreateAnnihilate`, [Physlib/QFT/PerturbationTheory/CreateAnnihilate.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/CreateAnnihilate.lean): 10 declarations (4 instances with no name), 6 with a docstring.

**`CreateAnnihilate`**, an inductive, [line 21](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/CreateAnnihilate.lean#L21).

> The type `CreateAnnihilate` is the type containing two elements `create` and `annihilate`.
> This type is used to specify if an operator is a creation, or annihilation, operator
> or the sum thereof or integral thereof etc.

```lean
inductive CreateAnnihilate where
  | create : CreateAnnihilate
  | annihilate : CreateAnnihilate
deriving Inhabited, BEq, DecidableEq
```

**An instance with no name**, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/CreateAnnihilate.lean#L29).

> The type `CreateAnnihilate` is finite.

```lean
instance : Fintype CreateAnnihilate
```

**`CreateAnnihilate.eq_create_or_annihilate`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/CreateAnnihilate.lean#L37).

```lean
lemma eq_create_or_annihilate (φ : CreateAnnihilate) : φ = create ∨ φ = annihilate
```

**`CreateAnnihilate.normalOrder`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/CreateAnnihilate.lean#L42).

> The normal ordering on creation and annihilation operators.
> Under this relation, `normalOrder a b` is false only if `a` is annihilate and `b` is create.

```lean
def normalOrder : CreateAnnihilate → CreateAnnihilate → Prop
```

**An instance with no name**, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/CreateAnnihilate.lean#L48).

> The normal ordering on `CreateAnnihilate` is decidable.

```lean
instance : (φ φ' : CreateAnnihilate) → Decidable (normalOrder φ φ')
```

**An instance with no name**, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/CreateAnnihilate.lean#L55).

> Normal ordering is total.

```lean
instance : Std.Total normalOrder
```

**An instance with no name**, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/CreateAnnihilate.lean#L59).

> Normal ordering is transitive.

```lean
instance : IsTrans CreateAnnihilate normalOrder
```

**`CreateAnnihilate.not_normalOrder_annihilate_iff_false`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/CreateAnnihilate.lean#L63).

```lean
lemma not_normalOrder_annihilate_iff_false (a : CreateAnnihilate) :
    (¬ normalOrder a annihilate) ↔ False
```

**`CreateAnnihilate.sum_eq`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/CreateAnnihilate.lean#L67).

```lean
lemma sum_eq {M : Type} [AddCommMonoid M] (f : CreateAnnihilate → M) :
    ∑ i, f i = f create + f annihilate
```

**`CreateAnnihilate.CreateAnnihilate_card_eq_two`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/CreateAnnihilate.lean#L73).

```lean
lemma CreateAnnihilate_card_eq_two : Fintype.card CreateAnnihilate = 2
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/QFT/PerturbationTheory/CreateAnnihilate.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/CreateAnnihilate.lean)
