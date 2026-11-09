---
declaration: def
origin: cited
lean: Exercise_A_1_3, Exercise_A_1_4, Exercise_A_1_5, Exercise_A_1_6
statement: formalized
---

# Appendix A.1: Mathematical Statements

> An introduction to mathematical statements.  Showcases some basic tactics and Lean syntax.

*Quoted from [Analysis/Appendix_A_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 6 labelled items, carried by 6 declarations: 2 stated without proof (2 of them exercises) and 4 definitions (4 with a value left as `sorry`). It also has 42 examples with no label, counted here but not shown.

## Exercise A.1.1

An `example` ([line 197](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_1.lean#L197)). An exercise, stated without proof.

> Exercise A.1.1.  Fill in the first `sorry` with something reasonable.

```lean
example {X Y:Prop} : ¬ ((X ∨ Y) ∧ ¬ (X ∧ Y)) ↔ sorry
```

## Exercise A.1.2

An `example` ([line 200](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_1.lean#L200)). An exercise, stated without proof.

> Exercise A.1.2.  Fill in the first `sorry` with something reasonable.

```lean
example {X Y:Prop} : ¬ (X ↔ Y) ↔ sorry
```

## Exercise A.1.3

`Exercise_A_1_3` (def, [line 203](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_1.lean#L203)). A definition whose value is left as `sorry`.

> Exercise A.1.3.

```lean
def Exercise_A_1_3 : Decidable (∀ (X Y: Prop), (X → Y) → (¬X → ¬ Y) → (X ↔ Y))
```

## Exercise A.1.4

`Exercise_A_1_4` (def, [line 209](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_1.lean#L209)). A definition whose value is left as `sorry`.

> Exercise A.1.4.

```lean
def Exercise_A_1_4 : Decidable (∀ (X Y: Prop), (X → Y) → (¬Y → ¬ X) → (X ↔ Y))
```

## Exercise A.1.5

`Exercise_A_1_5` (def, [line 214](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_1.lean#L214)). A definition whose value is left as `sorry`.

> Exercise A.1.5.

```lean
def Exercise_A_1_5 : Decidable (∀ (X Y Z: Prop), (X ↔ Y) → (Y ↔ Z) → [X,Y,Z].TFAE)
```

## Exercise A.1.6

`Exercise_A_1_6` (def, [line 219](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_1.lean#L219)). A definition whose value is left as `sorry`.

> Exercise A.1.6.

```lean
def Exercise_A_1_6 : Decidable (∀ (X Y Z: Prop), (X → Y) → (Y → Z) → (Z → X) → [X,Y,Z].TFAE)
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Appendix_A_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_1.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Appendix_A_1/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Appendix_A_1.html)
