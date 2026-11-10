---
declaration: theorem
origin: cited
lean: Erdos865.erdos865_upper_bound, Erdos865.sharpness
statement: formalized
proof: formalized
---

# A sharp 5/8 bound for Erdős Problem 865

> Formalizes the resolution of Erdős Problem 865 on pairwise sums. For A ⊆ {1,…,N}, a pairwise-sum triple is a set of distinct a, b, c ∈ A with a+b, a+c, b+c all in A, and A is triple-free when it has none. The development proves that every triple-free A ⊆ [1,N] satisfies 8·|A| ≤ 5·N + 53, that any A exceeding this bound contains a triple, and — via the construction A = [M,2M] ∪ [4M,8M] for N = 8M — that the constant 5/8 is optimal, so f₃(N) = 5N/8 + O(1). The upper bound runs through a folded additive lemma over ℤ/mℤ (a four-set union bound) and a folding lemma, closed by strong induction on N.

*Quoted from the card [LeanPool/projects/erdos865.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos865.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Erdos865.erdos865_upper_bound`](https://leanpool.github.io/lean-pool/LeanPool/Erdos865/Main.html#Erdos865.erdos865_upper_bound) (theorem; a main declaration), declared in [LeanPool/Erdos865/Main.lean, line 36](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos865/Main.lean#L36): “Every triple-free set A ⊆ [1,N] satisfies 8·|A| ≤ 5·N + 53, i.e. |A| ≤ (5/8)·N + O(1).”
- [`Erdos865.erdos865_contains_triple`](https://leanpool.github.io/lean-pool/LeanPool/Erdos865/Main.html#Erdos865.erdos865_contains_triple) (theorem), declared in [LeanPool/Erdos865/Main.lean, line 45](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos865/Main.lean#L45): “Every A ⊆ [1,N] with 5·N + 53 < 8·|A| contains a pairwise-sum triple (the paper's Theorem 1.1 form).”
- [`Erdos865.sharpness`](https://leanpool.github.io/lean-pool/LeanPool/Erdos865/Sharpness.html#Erdos865.sharpness) (theorem; a main declaration), declared in [LeanPool/Erdos865/Sharpness.lean, line 54](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos865/Sharpness.lean#L54): “For N = 8M with M ≥ 1 there is a triple-free A ⊆ [1,N] with 8·|A| = 5·N + 16, so the constant 5/8 is optimal.”

## Project

- Authors: Ricky Cipollini.
- Source: *A sharp 5/8 bound for an Erdős–Sós pairwise-sums problem*.
- Project repository: [mrricky22/erdos-865-lean](https://github.com/mrricky22/erdos-865-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11B75, 11B13.
- In Lean Pool: [LeanPool/Erdos865](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos865), from the card [LeanPool/projects/erdos865.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos865.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/erdos865.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos865.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Erdos865](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos865)
