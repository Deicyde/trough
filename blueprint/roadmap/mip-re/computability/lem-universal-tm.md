---
declaration: lemma
origin: cited
lean: MIPRE.Cost.exists_efficient_universal, MIPRE.Cost.exists_clocked_universal
statement: formalized
proof: formalized
---

# Efficient universal Turing machine

There is a program $u$ and a polynomial $p$ such that $\phi_u(e, x) = \phi_e(x)$ for all $e, x$, with $\mathrm{runtime}(u, (e,x)) \leq p\bigl(\left\vert {e} \right\vert, \left\vert {x} \right\vert, \mathrm{runtime}(e, x)\bigr)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Both the universal program and its clocked variant are self-interpreters of the ambient list language, written in the language itself (`MIPRE.Cost.Machine.univProg`, `MIPRE.Cost.Machine.univTProg`). Evaluation is first presented as an abstract machine on configurations (a control “evaluate $p$” or “return $v$”, an environment and a stack of frames) whose steps are charged exactly the costs of the evaluation rules, so that a derivation of cost $t$ corresponds to a machine run of at most $3t$ steps reaching a final configuration, and conversely every run reaching a final configuration comes from a derivation. Configurations are encoded as data and the step function is implemented by a fixed program (`stepProg`) at cost quadratic in the size of the configuration. Along the run simulating a derivation of cost $t$ on the input $x$, every configuration has size polynomial in $\left\vert {e} \right\vert + \left\vert {x} \right\vert + t$: values are results of sub-derivations, hence of size at most $t$; environments and stacks grow by at most one entry per unit of cost. The universal program iterates `stepProg` until a final configuration is reached, so its runs are polynomially bounded, and any of its halting runs is a machine run reaching a final configuration, hence a derivation with the same result. The clocked variant additionally carries, in unary, the remaining cost budget (decremented by the exact cost of each step), a step budget $3k+1$ guaranteeing termination, and a size guard $\Theta$, a fixed polynomial in $k + \left\vert {e} \right\vert + \left\vert {x} \right\vert$ dominating the configuration sizes of any run of cost at most $k$; it returns the timeout value when a budget or the guard is exceeded. The guard is checked on the configuration produced by each step, whose size is bounded by the cost of producing it, so the loop only handles configurations of polynomial size even when the simulated run does not halt.

## Lean

Formalized as [`MIPRE.Cost.exists_efficient_universal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.exists_efficient_universal), [`MIPRE.Cost.exists_clocked_universal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.exists_clocked_universal).

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 123](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L123)
