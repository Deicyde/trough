# Introduction

In this chapter, we explain how to construct families of loops to feed into the corrugation process explained at the end of the introduction.

Throughout this document, $E$ and $F$ will denote finite-dimensional real vector spaces.

- [loop](def-loop.md)

All of this chapter is devoted to proving the following proposition.

- [∃\_loops](prop-loops.md)

Let us briefly sketch the geometric idea behind the above proposition if we pretend there is only one point $x$, and drop it from the notation, and also focus only on $γ^1$. By assumption, there is a finite collection of points $p_i$ in $Ω$ and $λ_i ∈ [0, 1]$ such that $g$ is the barycenter $\sum λ_i p_i$. Since $Ω$ is open and connected, there is a smooth loop $γ_0$ which goes through each $p_i$. The claim is that $g$ is the average value of $γ = γ_0 ∘ h$ for some self-diffeomorphism $h$ of $𝕊^1$. The idea is to choose $h$ such that $γ$ rushes to $p_1$, stays there during a time roughly $λ_1$, rushes to $p_2$, etc. But, in order to achieve average exactly $g$, it seems like $h$ needs to be a discontinuous piecewise constant map. The assumption that $Ω$ is open means that the convex hull is open, which gives enough slack to get away with a smooth $h$.

In the previous proof sketch, there is a lot of freedom in constructing $γ$, which is problematic when trying to do it consistently when $x$ varies.
