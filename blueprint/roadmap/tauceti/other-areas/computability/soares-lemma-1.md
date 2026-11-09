---
declaration: theorem
origin: cited
lean: TauCeti.Oracle.Single.Code.computablePred_mem_stageLimit_of_eval_eq, TauCeti.Oracle.Single.Code.mem_stageLimit_iff_of_lt_agreementLength
statement: formalized
proof: formalized
---

# Soare's Lemma 1

Let `A` and `C` be the limits of monotone stages whose binary codes are
computable, and let requirement `e` hold, at every stage `s`, a restraint at least the agreement
restraint of the program `c` against `A s` with target `C s` and fuel `s`. If only finitely many
numbers injure `e`, and `c` relative to the limit of `A` computes the characteristic function of
the limit of `C`, then the limit of `C` is computable.

```lean
TauCeti.Oracle.Single.Code.computablePred_mem_stageLimit_of_eval_eq {A C : ℕ → Finset ℕ}
  {r : ℕ → ℕ → Option ℕ} {e : ℕ} {c : TauCeti.Oracle.Single.Code} (hA : Monotone A)
  (hC : Monotone C) (hAc : Computable fun s => Finset.equivBitIndices.symm (A s))
  (hCc : Computable fun s => Finset.equivBitIndices.symm (C s))
  (hr :
    ∀ (s : ℕ),
      ∃ b,
        r e s = some b ∧
          TauCeti.Oracle.Single.Code.agreementRestraint
              (TauCeti.Oracle.Single.Code.setAnswers ↑(A s)) s c ((↑(C s)).indicator 1) ≤
            b)
  (hI : (TauCeti.Priority.injurySet A r e).Finite)
  (heval :
    TauCeti.Oracle.Single.Code.eval (TauCeti.Enumeration.stageLimit A).oracle c =
      (TauCeti.Enumeration.stageLimit C).oracle) :
  ComputablePred fun x => x ∈ TauCeti.Enumeration.stageLimit C
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Oracle.Single.Code.computablePred_mem_stageLimit_of_eval_eq`](https://taucetiproject.org/docs/TauCeti/Computability/Priority/Agreement/Basic.html#TauCeti.Oracle.Single.Code.computablePred_mem_stageLimit_of_eval_eq).

## Other forms

**Soare's Lemma 1, correctness of late agreement.** Formalized in Tau Ceti as [`TauCeti.Oracle.Single.Code.mem_stageLimit_iff_of_lt_agreementLength`](https://taucetiproject.org/docs/TauCeti/Computability/Priority/Agreement/Basic.html#TauCeti.Oracle.Single.Code.mem_stageLimit_iff_of_lt_agreementLength).

```lean
TauCeti.Oracle.Single.Code.mem_stageLimit_iff_of_lt_agreementLength {A C : ℕ → Finset ℕ}
  {r : ℕ → ℕ → Option ℕ} {e s x : ℕ} {c : TauCeti.Oracle.Single.Code} {s₀ : ℕ} (hA : Monotone A)
  (hC : Monotone C)
  (hr :
    ∀ (s : ℕ),
      s₀ ≤ s →
        ∃ b,
          r e s = some b ∧
            TauCeti.Oracle.Single.Code.agreementRestraint
                (TauCeti.Oracle.Single.Code.setAnswers ↑(A s)) s c ((↑(C s)).indicator 1) ≤
              b)
  (hI : ∀ (s : ℕ), s₀ ≤ s → TauCeti.Priority.injuriesAt A r e s = ∅)
  (heval :
    ∀ y ≤ x,
      TauCeti.Oracle.Single.Code.eval (TauCeti.Enumeration.stageLimit A).oracle c y =
        (TauCeti.Enumeration.stageLimit C).oracle y)
  (hs : s₀ ≤ s)
  (hx :
    x <
      TauCeti.Oracle.Single.Code.agreementLength (TauCeti.Oracle.Single.Code.setAnswers ↑(A s)) s c
        ((↑(C s)).indicator 1)) :
  x ∈ TauCeti.Enumeration.stageLimit C ↔ x ∈ C s
```

## Sources

- [Tau Ceti documentation: `TauCeti.Oracle.Single.Code.computablePred_mem_stageLimit_of_eval_eq`](https://taucetiproject.org/docs/TauCeti/Computability/Priority/Agreement/Basic.html#TauCeti.Oracle.Single.Code.computablePred_mem_stageLimit_of_eval_eq)
- [Source of `TauCeti.Oracle.Single.Code.computablePred_mem_stageLimit_of_eval_eq` in TauCeti/Computability/Priority/Agreement/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Computability/Priority/Agreement/Basic.lean#L147)
