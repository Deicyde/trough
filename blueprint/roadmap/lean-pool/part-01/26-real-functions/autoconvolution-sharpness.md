---
declaration: theorem
origin: cited
lean: Autoconvolutions.sharpness
statement: formalized
proof: formalized
---

# Sharpness of the Martin–O’Bryant autoconvolution inequality

> Proves that nonzero nonnegative finite step functions on the real line have autoconvolution norm ratios arbitrarily close to one. The ratio is the squared L2 norm divided by the product of the L1 and essential-supremum norms, all for Lebesgue measure. Develops polynomial coefficient blocks, digit separation, collision estimates, and reusable convolution plateau bounds.

*Quoted from the card [LeanPool/projects/autoconvolution-sharpness.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/autoconvolution-sharpness.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Autoconvolutions.sharpness`](https://leanpool.github.io/lean-pool/LeanPool/AutoconvolutionSharpness/Sharpness.html#Autoconvolutions.sharpness) (theorem; a main declaration), declared in [LeanPool/AutoconvolutionSharpness/Sharpness.lean, line 24](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/AutoconvolutionSharpness/Sharpness.lean#L24): “For every positive real epsilon, some finite sequence of nonnegative real heights, including a positive height, gives a step function on successive integer unit intervals whose autoconvolution norm ratio exceeds one minus epsilon.”
- [`Autoconvolutions.Construction.witness_ratio_lower`](https://leanpool.github.io/lean-pool/LeanPool/AutoconvolutionSharpness/Main.html#Autoconvolutions.Construction.witness_ratio_lower) (theorem), declared in [LeanPool/AutoconvolutionSharpness/Main.lean, line 32](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/AutoconvolutionSharpness/Main.lean#L32): “The explicitly constructed polynomial gives a quantitative lower bound for the Lebesgue autoconvolution ratio in terms of factorial and geometric factors.”
- [`Autoconvolutions.blocks_energy_le`](https://leanpool.github.io/lean-pool/LeanPool/AutoconvolutionSharpness/Bounds.html#Autoconvolutions.blocks_energy_le) (theorem), declared in [LeanPool/AutoconvolutionSharpness/Bounds.lean, line 114](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/AutoconvolutionSharpness/Bounds.lean#L114): “An injectively indexed family of separated coefficient plateaus supplies a lower bound on the squared L2 norm of a step function's autoconvolution.”

## Project

- Authors: Tonći Crmarić, Vjekoslav Kovač, Jelena Rupčić.
- Source: *Sharpness of the Martin–O’Bryant autoconvolution inequality*, [arXiv:2611.12685](https://arxiv.org/abs/2611.12685).
- Project repository: [VjekoKovac/lean-autoconvolutions](https://github.com/VjekoKovac/lean-autoconvolutions), at commit [e6a8e691](https://github.com/VjekoKovac/lean-autoconvolutions/tree/e6a8e69129f67621693430dceeae42050377ffa6).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 26D15, 42A85.
- In Lean Pool: [LeanPool/AutoconvolutionSharpness](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/AutoconvolutionSharpness), from the card [LeanPool/projects/autoconvolution-sharpness.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/autoconvolution-sharpness.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/autoconvolution-sharpness.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/autoconvolution-sharpness.yaml)
- [Lean Pool at 307e3125: LeanPool/AutoconvolutionSharpness](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/AutoconvolutionSharpness)
