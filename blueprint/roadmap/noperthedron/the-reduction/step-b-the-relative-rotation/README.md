# Step B: the relative rotation

Fix the outer rotation $s = s(u, v)$ and write the inner rotation as $s\,Q$, so that $Q = s^T R_i$ is the *relative rotation*. The moves of Lemma [Symmetries](../moves-that-preserve-rupert-pairs/lem-move-sym.md) (inner) and Lemma [Inner half-turn](../moves-that-preserve-rupert-pairs/lem-move-halfturn.md) act on $Q$ without changing $s$: $Q \mapsto Q g_k$ and $Q \mapsto H Q$, where $H = s^T R_z(\pi) s$ is the half-turn about the view. The orbit $\{ H^e Q g_k : e \in \{0, 1\},\ 0 \le k < 15 \}$ has at most 30 elements.

The poses that are hardest to exclude are the *aligned* ones, where the inner and outer shadows coincide. The obvious ones have $Q = I$. A second family comes from the following rotation, which is not a symmetry of $\operatorname{\mathbf{P}}$.

- [tau](def-tau.md)
- [tau_pair](lem-tau-pair.md)

Since $\sigma$ is a bijection of the 30 points $\mathcal{C}_{30} \cdot C_3$, the rotation $\tau$ maps these points onto themselves.

The view straight down the $z$-axis shows only the copies of $C_3$ on the boundary of the shadow, and so do nearby views. For such views the pose with $Q = \tau$ is therefore aligned, even though $\tau \operatorname{\mathbf{P}} \ne \operatorname{\mathbf{P}}$. To handle both families, choose the representative of the orbit that is closest to $I$ or to $\tau$.

- [orbit_score](def-orbit-score.md)

The bias $1/8$ breaks the ties at the isolated horizontal views where $H g_k = \tau$, in favour of $I$.

- [step_orbit](lem-step-orbit.md)
