from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Wine


class WineListView(LoginRequiredMixin, ListView):
    """
    Display a list of wines in the inventory.
    """

    model = Wine
    template_name = "vinventory/wine_list.html"
    context_object_name = "wines"

    def get_queryset(self):
        """
        Return the wines filtered by the logged-in user.
        """
        return Wine.objects.filter(user=self.request.user)

    def get_success_url(self):
        """
        Return the URL to redirect to after successful operations.
        """
        return reverse_lazy("vinventory:wine_list")

    def drink_wine(self, pk):
        """
        Decrease the quantity of a wine and save the changes.
        """
        wine = Wine.objects.get(pk=pk)
        if wine.quantity > 0:
            wine.quantity -= 1
            wine.save()
        return HttpResponseRedirect(
            self.request.META.get("HTTP_REFERER", "/")
        )  # Redirect back to the same page

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests, including the 'drink' action.
        """
        if "drink" in request.POST:
            wine_pk = request.POST.get("wine_pk")
            self.drink_wine(wine_pk)
        return self.get(request, *args, **kwargs)


class WineCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new wine entry in the inventory.
    """

    model = Wine
    template_name = "vinventory/wine_form.html"
    fields = [
        "name",
        "variety",
        "region",
        "year",
        "quantity",
        "received_from",
        "date_received",
        "date_to_drink_start",
        "date_to_drink_end",
    ]

    def form_valid(self, form):
        """
        Set the current user as the owner of the new wine entry.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """
        Return the URL to redirect to after successful creation.
        """
        return reverse_lazy("vinventory:wine_list")


class WineUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update an existing wine entry in the inventory.
    """

    model = Wine
    template_name = "vinventory/wine_form.html"
    fields = [
        "name",
        "variety",
        "region",
        "year",
        "quantity",
        "received_from",
        "date_received",
        "date_to_drink_start",
        "date_to_drink_end",
    ]

    def get_queryset(self):
        """
        Return the wines filtered by the logged-in user.
        """
        return Wine.objects.filter(user=self.request.user)

    def get_success_url(self):
        """
        Return the URL to redirect to after successful update.
        """
        return reverse_lazy("vinventory:wine_list")


class WineDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting a wine entry from the inventory.

    Inherits from Django's DeleteView and requires user login.

    Attributes:
        model (class): The model class representing the Wine data.
        template_name (str): The name of the template used for the deletion confirmation page.
        success_url (str): The URL to redirect to after successful deletion.

    Methods:
        get_queryset(): Return the wines filtered by the logged-in user.
        get_success_url(): Return the URL to redirect to after successful deletion.
    """

    model = Wine
    template_name = "vinventory/wine_confirm_delete.html"
    success_url = reverse_lazy("vinventory:wine_list")

    def get_queryset(self):
        """
        Return the queryset of wines filtered by the logged-in user.

        Returns:
            QuerySet: A QuerySet of Wine objects.
        """
        return Wine.objects.filter(user=self.request.user)

    def get_success_url(self):
        """
        Return the URL to redirect to after successful deletion.

        Returns:
            str: The URL for the wine list view.
        """
        return reverse_lazy("vinventory:wine_list")
