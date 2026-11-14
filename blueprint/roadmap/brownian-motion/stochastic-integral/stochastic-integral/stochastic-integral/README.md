# Stochastic integral

TODO: relax continuity of the martingales, be clear about continuous quadratic variation vs general càdlàg quadratic variation.

For $M$ a local martingale and $X$ a stochastic process, we will use integrals of the form $\int_0^t X_s \: d\langle M \rangle_s$ . Let's explain what those integrals mean. For all $\omega \in \Omega$, $\langle M \rangle(\omega)$ is a right-continuous non-decreasing function (called a Stieltjes function in Mathlib) so it defines a measure on $\mathbb{R}_+$, denoted by $d\langle M \rangle$ . Then, for each fixed $\omega \in \Omega$, if the function $s \mapsto X_s(\omega)$ is integrable with respect to the measure $d\langle M \rangle(\omega)$, the Bochner integral $\int_0^t X_s(\omega) \: d\langle M \rangle(\omega)$ is well-defined. By $\int_0^t X_s \: d\langle M \rangle_s$, we mean the random variable $\omega \mapsto \int_0^t X_s(\omega) \: d\langle M \rangle(\omega)$ . If we also vary $t$, we get a stochastic process.

## Itô isometry

- [Filtration.predictable_le_prod](lem-filtration-predictable-le-prod.md)
- [L2 space of predictable processes](def-l2predictable.md)

TODO: the measures should be at least finite, I guess.

TODO: we will write that a stochastic process $X : T \to \Omega \to E$ “is in $L^2(\mu, P)$”, but this means that the L2 equivalence class of the function $(t, \omega) \mapsto X_t(\omega)$ is in $L^2(\mu, P)$ . In Lean, we can use `MemLp` for the uncurried function.
