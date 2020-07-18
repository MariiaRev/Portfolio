function applyCallback(i)
{
	$(".arrow"+i).click(function()
	{
		$(".more"+i).toggle();
	})
}
$(document).ready(
	function()
	{
		$(".to-pic").click(function()
		{
			$(".text-review").hide();
			$(".works").show();
		})
		$(".to-text").click(function()
		{
			$(".works").hide();
			$(".text-review").show();
		})
		for (var i=1; i<=6; i++)
		{
			applyCallback(i);
		}
	}
)
